from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

from utils.normalization import (
    normalize_sleep, normalize_study, normalize_screen,
    normalize_activity, normalize_mood
)
from utils.stress_classifier import classify_stress_from_scores
from routes.checkin_routes import checkin_bp
from routes.chatbot_routes import chatbot_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(checkin_bp)
app.register_blueprint(chatbot_bp)

try:
    with open("../ml/ml/stress_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("../ml/ml/label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)
    MODEL_LOADED = True
except FileNotFoundError:
    MODEL_LOADED = False


@app.route("/predict", methods=["POST"])
def predict():
    if not MODEL_LOADED:
        return jsonify({
            "status": "error",
            "message": "ML model not available"
        }), 503
    
    data = request.get_json()
    features = np.array([[  
        data["sleep"],
        data["study"],
        data["screen"],
        data["activity"],
        data["mood"]
    ]])

    prediction = model.predict(features)
    stress_label = label_encoder.inverse_transform(prediction)[0]

    return jsonify({
        "predicted_stress": stress_label
    })


@app.route("/ikigai", methods=["POST"])
def ikigai():
    data = request.get_json()

    sleep_score = normalize_sleep(data["sleep"])
    study_score = normalize_study(data["study"])
    screen_score = normalize_screen(data["screen"])
    activity_score = normalize_activity(data["activity"])
    mood_score = normalize_mood(data["mood"])

    stress_score = (
        0.30 * sleep_score +
        0.25 * mood_score +
        0.20 * screen_score +
        0.15 * study_score +
        0.10 * activity_score
    )

    rule_based_stress = classify_stress_from_scores(
        sleep_score, screen_score, mood_score, activity_score
    )

    productivity_score = (
        0.40 * study_score +
        0.30 * sleep_score +
        0.20 * activity_score +
        0.10 * screen_score
    )

    love = (mood_score + activity_score) / 2
    good_at = study_score
    need = (sleep_score + (100 - stress_score)) / 2
    value = productivity_score
    ikigai_score = (love + good_at + need + value) / 4

    ml_stress = None
    if MODEL_LOADED:
        features = np.array([[  
            data["sleep"],
            data["study"],
            data["screen"],
            data["activity"],
            data["mood"]
        ]])
        ml_prediction = model.predict(features)
        ml_stress = label_encoder.inverse_transform(ml_prediction)[0]

    final_stress = rule_based_stress
    if data["sleep"] < 4 or data["mood"] <= 2:
        final_stress = "MEDIUM"
    if data["sleep"] < 3 and data["screen"] > 6:
        final_stress = "HIGH"

    response = {
        "layer1_normalized": {
            "sleep_score": round(sleep_score, 2),
            "study_score": round(study_score, 2),
            "screen_score": round(screen_score, 2),
            "activity_score": round(activity_score, 2),
            "mood_score": round(mood_score, 2)
        },
        "layer2_scores": {
            "stress_score": round(stress_score, 2),
            "rule_based_stress": rule_based_stress,
            "productivity_score": round(productivity_score, 2)
        },
        "layer3_ikigai": {
            "love": round(love, 2),
            "good_at": round(good_at, 2),
            "need": round(need, 2),
            "value": round(value, 2),
            "ikigai_score": round(ikigai_score, 2)
        }
    }
    
    if MODEL_LOADED:
        response["layer3_ml_support"] = {
            "ml_predicted_stress": ml_stress,
            "final_stress_level": final_stress
        }
    else:
        response["layer3_ml_support"] = {
            "ml_predicted_stress": None,
            "final_stress_level": final_stress,
            "note": "ML model not available"
        }

    return jsonify(response)


@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "message": "Mental Wellness Platform API",
        "endpoints": {
            "checkin": "/checkin (POST)",
            "chatbot": "/chatbot (POST)",
            "chatbot_modes": "/chatbot/modes (GET)",
            "predict": "/predict (POST)",
            "ikigai": "/ikigai (POST)"
        }
    })


if __name__ == "__main__":
    app.run(debug=True)
