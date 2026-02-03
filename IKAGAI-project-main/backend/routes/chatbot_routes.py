from flask import Blueprint, request, jsonify
import os
from services.chatbot_service import get_chatbot_response

chatbot_bp = Blueprint('chatbot', __name__)


@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                "status": "error",
                "message": "Missing required field: 'message'"
            }), 400
        
        message = data['message'].strip()
        
        if not message:
            return jsonify({
                "status": "error",
                "message": "Message cannot be empty"
            }), 400
        
        mode = data.get('mode', 'listener')
        if mode not in ['listener', 'motivator', 'advisor']:
            mode = 'listener'
        
        conversation_history = data.get('conversation_history', [])
        api_key = os.getenv('OPENAI_API_KEY') or os.getenv('LLM_API_KEY')
        
        response = get_chatbot_response(
            message=message,
            mode=mode,
            conversation_history=conversation_history,
            api_key=api_key
        )
        
        return jsonify({
            "status": "success",
            **response
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Internal server error: {str(e)}"
        }), 500


@chatbot_bp.route('/chatbot/modes', methods=['GET'])
def get_chatbot_modes():
    modes = [
        {
            "id": "listener",
            "name": "Listener",
            "description": "Empathetic, supportive responses. I'm here to listen and validate your feelings."
        },
        {
            "id": "motivator",
            "name": "Motivator",
            "description": "Encouraging, uplifting responses. I'm here to help you see your strength and progress."
        },
        {
            "id": "advisor",
            "name": "Advisor",
            "description": "Gentle, thoughtful suggestions. I'm here to offer wellness tips and coping strategies."
        }
    ]
    
    return jsonify({
        "status": "success",
        "modes": modes
    }), 200
