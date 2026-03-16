from datetime import datetime, timedelta

schedule = {}

def generate_schedule():
    doctors = ["Dr. Smith", "Dr. Patel", "Dr. Chen", "Dr. Rodriguez"]

    for doctor in doctors:
        slots = []
        for i in range(1, 30):
            day = datetime.now() + timedelta(days=i)
            slots.append(day.strftime("%Y-%m-%d 10:00"))
            slots.append(day.strftime("%Y-%m-%d 14:00"))

        schedule[doctor] = slots


generate_schedule()


def get_slots(doctor_name):
    return schedule.get(doctor_name, [])


def book_slot(doctor_name, slot):
    if slot in schedule.get(doctor_name, []):
        schedule[doctor_name].remove(slot)
        return True
    return False