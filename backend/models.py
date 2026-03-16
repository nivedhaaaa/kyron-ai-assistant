from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    session_id: str


class AppointmentRequest(BaseModel):
    first_name: str
    last_name: str
    dob: str
    phone: str
    email: str
    body_part: str