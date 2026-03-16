from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import ChatRequest, AppointmentRequest
from doctors import match_doctor
from scheduler import get_slots, book_slot
from safety import check_safety
from ai_agent import ai_chat
from email_service import send_email
from voice_routes import router as voice_router

app = FastAPI()
app.include_router(voice_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Kyron Medical AI Assistant"}

@app.post("/chat")
def chat(req: ChatRequest):

    if not check_safety(req.message):
        return {"response": "I cannot provide medical advice."}

    response = ai_chat(req.message)

    return {"response": response}


@app.post("/match_doctor")
def doctor_match(body_part: str):

    doc = match_doctor(body_part)

    if not doc:
        return {"message": "We do not treat that body part"}

    slots = get_slots(doc["name"])

    return {
        "doctor": doc,
        "available_slots": slots[:5] if slots else []
    }


@app.post("/book")
def book(req: AppointmentRequest):

    doc = match_doctor(req.body_part)

    if not doc:
        return {"message": "No doctor available for that body part"}

    slots = get_slots(doc["name"])

    if not slots:
        return {"message": "No available slots"}

    slot = slots[0]

    book_slot(doc["name"], slot)

    appointment = f"{doc['name']} at {slot}"

    send_email(req.email, appointment)

    return {
        "message": "Appointment confirmed",
        "doctor": doc["name"],
        "time": slot
    }