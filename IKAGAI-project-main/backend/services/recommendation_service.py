def get_stress_recommendations(stress_level):
    recommendations = {
        "stress_level": stress_level,
        "recommendations": []
    }
    
    if stress_level == "LOW":
        recommendations["recommendations"] = [
            {
                "type": "mindfulness",
                "title": "Maintain Your Balance",
                "description": "You're doing well! Keep up these healthy habits.",
                "actions": [
                    "Continue your current routine",
                    "Practice 5-minute daily mindfulness",
                    "Stay connected with friends and family",
                    "Maintain regular sleep schedule"
                ]
            }
        ]
    
    elif stress_level == "MEDIUM":
        recommendations["recommendations"] = [
            {
                "type": "breathing",
                "title": "Guided Breathing Exercise",
                "description": "Take a moment to practice deep breathing to help manage stress.",
                "actions": [
                    "Try 4-7-8 breathing: Inhale 4s, Hold 7s, Exhale 8s",
                    "Practice for 5-10 minutes",
                    "Find a quiet space"
                ]
            },
            {
                "type": "meditation",
                "title": "Short Meditation Session",
                "description": "A brief meditation can help reset your mind and reduce tension.",
                "actions": [
                    "Try a 10-minute guided meditation",
                    "Focus on your breath",
                    "Use a meditation app or audio guide"
                ]
            }
        ]
    
    else:  # HIGH
        recommendations["recommendations"] = [
            {
                "type": "chatbot",
                "title": "Talk to Our Wellness Chatbot",
                "description": "Have a supportive conversation with our AI wellness companion.",
                "actions": [
                    "Visit /chatbot endpoint",
                    "Choose a conversation mode that feels right",
                    "Express what you're feeling"
                ]
            },
            {
                "type": "professional",
                "title": "Consider Professional Support",
                "description": "If you're experiencing persistent stress, consider speaking with a mental health professional.",
                "actions": [
                    "Contact your campus counseling center",
                    "Reach out to a therapist or counselor",
                    "Call a mental health helpline if needed"
                ],
                "resources": [
                    "National Suicide Prevention Lifeline: 988",
                    "Crisis Text Line: Text HOME to 741741",
                    "Your local mental health services"
                ]
            },
            {
                "type": "immediate",
                "title": "Immediate Self-Care",
                "description": "Take care of yourself right now with these gentle steps.",
                "actions": [
                    "Step away from screens for 15 minutes",
                    "Drink water and take deep breaths",
                    "Move your body gently (stretch or walk)",
                    "Reach out to someone you trust"
                ]
            }
        ]
    
    return recommendations
