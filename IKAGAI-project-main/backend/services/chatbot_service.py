import os
from typing import Optional, List, Dict

SAFETY_DISCLAIMER = (
    "⚠️ **Important**: I'm here to provide supportive conversation, not medical advice. "
    "If you're experiencing a mental health crisis, please contact a professional immediately. "
    "This chatbot is not a replacement for therapy or professional mental health care."
)

HELP_RESOURCES = [
    "National Suicide Prevention Lifeline: 988",
    "Crisis Text Line: Text HOME to 741741",
    "Your campus counseling center or local mental health services"
]


def detect_crisis_keywords(message: str) -> bool:
    crisis_keywords = [
        "suicide", "kill myself", "end it all", "want to die",
        "self harm", "hurt myself", "no point", "give up"
    ]
    message_lower = message.lower()
    return any(keyword in message_lower for keyword in crisis_keywords)


def get_chatbot_response(
    message: str,
    mode: str = "listener",
    conversation_history: Optional[List[Dict]] = None,
    api_key: Optional[str] = None
) -> Dict:
    if detect_crisis_keywords(message):
        return {
            "response": (
                "I'm really concerned about what you've shared. Your feelings are valid and important. "
                "Please reach out to a mental health professional immediately. "
                "You can call 988 (National Suicide Prevention Lifeline) or text HOME to 741741. "
                "You don't have to go through this alone - there are people who want to help."
            ),
            "mode": mode,
            "crisis_detected": True,
            "resources": HELP_RESOURCES,
            "disclaimer": SAFETY_DISCLAIMER
        }
    
    if api_key:
        return _get_llm_response(message, mode, conversation_history, api_key)
    
    return _get_rule_based_response(message, mode)


def _get_llm_response(
    message: str,
    mode: str,
    conversation_history: Optional[List[Dict]],
    api_key: str
) -> Dict:
    try:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            use_new_api = True
        except ImportError:
            import openai
            openai.api_key = api_key
            use_new_api = False
        
        system_prompts = {
            "listener": (
                "You are a supportive, empathetic listener. Your role is to: "
                "- Listen actively and validate feelings "
                "- Show empathy and understanding "
                "- Ask gentle, open-ended questions "
                "- Never provide medical advice or diagnosis "
                "- Always include a safety disclaimer about professional help "
                "- Be warm, non-judgmental, and supportive"
            ),
            "motivator": (
                "You are an encouraging, positive motivator. Your role is to: "
                "- Provide gentle encouragement and hope "
                "- Acknowledge strengths and progress "
                "- Offer positive reframing when appropriate "
                "- Never provide medical advice or diagnosis "
                "- Always include a safety disclaimer about professional help "
                "- Be uplifting but realistic, not dismissive"
            ),
            "advisor": (
                "You are a gentle, thoughtful advisor. Your role is to: "
                "- Offer gentle suggestions and coping strategies "
                "- Share general wellness tips (not medical advice) "
                "- Help explore options and possibilities "
                "- Never provide medical advice or diagnosis "
                "- Always include a safety disclaimer about professional help "
                "- Be supportive and non-prescriptive"
            )
        }
        
        system_prompt = system_prompts.get(mode, system_prompts["listener"])
        messages = [{"role": "system", "content": system_prompt}]
        
        if conversation_history:
            for msg in conversation_history[-5:]:
                messages.append({
                    "role": msg.get("role", "user"),
                    "content": msg.get("content", "")
                })
        
        messages.append({"role": "user", "content": message})
        
        if use_new_api:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=300,
                temperature=0.7
            )
            bot_response = response.choices[0].message.content
        else:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=300,
                temperature=0.7
            )
            bot_response = response.choices[0].message.content
        
        return {
            "response": bot_response,
            "mode": mode,
            "crisis_detected": False,
            "disclaimer": SAFETY_DISCLAIMER
        }
        
    except (ImportError, Exception):
        return _get_rule_based_response(message, mode)


def _get_rule_based_response(message: str, mode: str) -> Dict:
    message_lower = message.lower()
    
    if mode == "listener":
        if any(word in message_lower for word in ["sad", "down", "depressed", "unhappy"]):
            response = (
                "I hear that you're feeling down, and I want you to know that your feelings are valid. "
                "It's okay to not be okay sometimes. Would you like to talk more about what's been going on?"
            )
        elif any(word in message_lower for word in ["anxious", "worried", "nervous", "stressed"]):
            response = (
                "It sounds like you're experiencing some anxiety or worry. That can feel really overwhelming. "
                "What's been contributing to these feelings? I'm here to listen."
            )
        elif any(word in message_lower for word in ["tired", "exhausted", "drained"]):
            response = (
                "Feeling tired and drained can make everything feel harder. "
                "How have you been sleeping? Sometimes rest is one of the most important things we can do for ourselves."
            )
        else:
            response = (
                "Thank you for sharing that with me. I'm listening, and I want to understand what you're going through. "
                "Can you tell me more about how you're feeling?"
            )
    
    elif mode == "motivator":
        if any(word in message_lower for word in ["can't", "impossible", "too hard", "give up"]):
            response = (
                "I understand things feel really difficult right now. But you've made it through tough times before, "
                "and you have strength within you. What's one small step you could take today?"
            )
        elif any(word in message_lower for word in ["progress", "better", "improving"]):
            response = (
                "That's wonderful to hear! Acknowledging progress, even small steps, is important. "
                "You're doing the work, and that matters. What's been helping you move forward?"
            )
        else:
            response = (
                "You're taking a positive step by reaching out and talking about this. "
                "Remember, healing and growth aren't always linear, but you're moving forward. "
                "What's something you're proud of yourself for today?"
            )
    
    else:  # advisor
        if any(word in message_lower for word in ["sleep", "tired", "rest"]):
            response = (
                "Sleep is so important for our mental wellness. Have you tried establishing a bedtime routine? "
                "Things like reducing screen time before bed, keeping a consistent sleep schedule, "
                "or doing some light reading can help. What does your current sleep routine look like?"
            )
        elif any(word in message_lower for word in ["stress", "overwhelmed", "pressure"]):
            response = (
                "When stress feels overwhelming, breaking things down can help. "
                "Have you tried deep breathing exercises, taking short breaks, or writing down what's on your mind? "
                "Sometimes just acknowledging what we're feeling can help us manage it better."
            )
        else:
            response = (
                "It sounds like you're looking for some guidance. While I can't provide medical advice, "
                "I can suggest some general wellness practices: regular movement, staying connected with others, "
                "practicing mindfulness, and ensuring you're taking care of your basic needs. "
                "What area would you like to explore?"
            )
    
    return {
        "response": response,
        "mode": mode,
        "crisis_detected": False,
        "disclaimer": SAFETY_DISCLAIMER
    }
