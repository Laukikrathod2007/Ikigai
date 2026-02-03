from flask import Blueprint, request, jsonify
from utils.stress_classifier import classify_stress
from utils.normalization import (
    normalize_sleep, normalize_screen, normalize_mood, normalize_activity
)
from services.recommendation_service import get_stress_recommendations

checkin_bp = Blueprint('checkin', __name__)


@checkin_bp.route('/checkin', methods=['POST'])
def daily_checkin():
    try:
        data = request.get_json()
        
        required_fields = ['sleep_hours', 'screen_time', 'mood', 'physical_activity']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "status": "error",
                    "message": f"Missing required field: {field}"
                }), 400
        
        sleep_hours = int(data['sleep_hours'])
        screen_time = int(data['screen_time'])
        mood = int(data['mood'])
        physical_activity = int(data['physical_activity'])
        
        if not (1 <= mood <= 5):
            return jsonify({
                "status": "error",
                "message": "mood must be between 1 and 5"
            }), 400
        
        if sleep_hours < 0 or screen_time < 0 or physical_activity < 0:
            return jsonify({
                "status": "error",
                "message": "Values cannot be negative"
            }), 400
        
        stress_level = classify_stress(sleep_hours, screen_time, mood, physical_activity)
        
        sleep_score = normalize_sleep(sleep_hours)
        screen_score = normalize_screen(screen_time)
        mood_score = normalize_mood(mood)
        activity_score = normalize_activity(physical_activity)
        
        recommendations = get_stress_recommendations(stress_level)
        
        return jsonify({
            "status": "success",
            "checkin_data": {
                "sleep_hours": sleep_hours,
                "screen_time": screen_time,
                "mood": mood,
                "physical_activity": physical_activity,
                "normalized_scores": {
                    "sleep_score": round(sleep_score, 2),
                    "screen_score": round(screen_score, 2),
                    "mood_score": round(mood_score, 2),
                    "activity_score": round(activity_score, 2)
                }
            },
            "stress_level": stress_level,
            "recommendations": recommendations,
            "disclaimer": (
                "This assessment is for awareness and self-reflection only. "
                "It is not a medical diagnosis. If you're experiencing persistent distress, "
                "please consider speaking with a mental health professional."
            )
        }), 200
        
    except ValueError as e:
        return jsonify({
            "status": "error",
            "message": f"Invalid data type: {str(e)}"
        }), 400
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Internal server error: {str(e)}"
        }), 500
