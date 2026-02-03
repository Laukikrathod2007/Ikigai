def normalize_sleep(sleep):
    if 7 <= sleep <= 8:
        return 100
    elif 6 <= sleep < 7 or 8 < sleep <= 9:
        return 80
    elif 5 <= sleep < 6 or 9 < sleep <= 10:
        return 60
    else:
        return 30


def normalize_study(study):
    if 4 <= study <= 6:
        return 90
    elif 2 <= study < 4 or 6 < study <= 8:
        return 75
    else:
        return 50


def normalize_screen(screen):
    if screen <= 2:
        return 90
    elif screen <= 4:
        return 75
    elif screen <= 6:
        return 50
    else:
        return 30


def normalize_activity(activity):
    if activity >= 30:
        return 90
    elif activity >= 15:
        return 70
    else:
        return 40


def normalize_mood(mood):
    return (mood / 5) * 100
