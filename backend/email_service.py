import smtplib

def send_email(to_email, appointment):
    print(f"Sending confirmation email to {to_email}")

    message = f"""
    Your appointment is confirmed.

    {appointment}
    """

    print(message)