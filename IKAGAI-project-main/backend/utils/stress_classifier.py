def classify_stress(sleep_hours, screen_time, mood, physical_activity):
    stress_score = 0
    
    if sleep_hours >= 7 and sleep_hours <= 8:
        stress_score += 30
    elif sleep_hours >= 6 and sleep_hours < 9:
        stress_score += 20
    elif sleep_hours >= 5:
        stress_score += 10
    
    if mood >= 4:
        stress_score += 30
    elif mood == 3:
        stress_score += 20
    elif mood == 2:
        stress_score += 10
    
    if screen_time <= 2:
        stress_score += 20
    elif screen_time <= 4:
        stress_score += 15
    elif screen_time <= 6:
        stress_score += 10
    else:
        stress_score += 5
    
    if physical_activity >= 30:
        stress_score += 20
    elif physical_activity >= 15:
        stress_score += 15
    else:
        stress_score += 10
    
    if stress_score >= 70:
        return "LOW"
    elif stress_score >= 40:
        return "MEDIUM"
    else:
        return "HIGH"


def classify_stress_from_scores(sleep_score, screen_score, mood_score, activity_score):
    stress_score = (
        0.30 * sleep_score +
        0.25 * mood_score +
        0.20 * screen_score +
        0.20 * activity_score
    )
    
    if stress_score >= 75:
        return "LOW"
    elif stress_score >= 50:
        return "MEDIUM"
    else:
        return "HIGH"
