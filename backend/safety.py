blocked_words = [
    "diagnose",
    "treatment plan",
    "medical advice",
    "prescribe"
]


def check_safety(message: str):
    for word in blocked_words:
        if word in message.lower():
            return False
    return True