doctors = [
    {
        "name": "Dr. Smith",
        "specialty": "heart",
        "body_part": "heart"
    },
    {
        "name": "Dr. Patel",
        "specialty": "knee",
        "body_part": "knee"
    },
    {
        "name": "Dr. Chen",
        "specialty": "skin",
        "body_part": "skin"
    },
    {
        "name": "Dr. Rodriguez",
        "specialty": "eye",
        "body_part": "eye"
    }
]


def match_doctor(body_part: str):
    for doc in doctors:
        if body_part.lower() in doc["body_part"]:
            return doc
    return None