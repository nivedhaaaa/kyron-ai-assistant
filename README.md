# Kyron Medical AI Assistant

An AI-powered medical scheduling assistant that helps patients find doctors, view appointment slots, and book appointments through a conversational interface.

## Features

- AI chat assistant for scheduling support
- Doctor matching by body part
- 30-day appointment availability
- Appointment booking with confirmation
- Voice handoff endpoint
- Customer-facing web interface
- FastAPI backend deployed on AWS EC2

## Tech Stack

Backend:
- FastAPI
- Python

Frontend:
- HTML
- CSS
- JavaScript

Deployment:
- AWS EC2

## Public Demo

Web App:
http://18.191.25.105:8000/app

API Docs:
http://18.191.25.105:8000/docs

## Project Structure

backend/
- main.py
- doctors.py
- scheduler.py
- models.py
- safety.py
- ai_agent.py
- voice_routes.py

frontend/
- index.html
- app.js
- style.css

## Example Workflow

1. User enters patient information
2. System matches doctor based on body part
3. Available slots are displayed
4. Appointment is booked
5. Confirmation is sent
6. User can continue conversation via voice AI