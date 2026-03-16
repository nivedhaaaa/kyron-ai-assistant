from fastapi import APIRouter

router = APIRouter()

@router.post("/voice")
def voice_call():
    return {
        "message": "Voice AI call initiated"
    }