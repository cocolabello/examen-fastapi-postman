from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


class Event(BaseModel):
    title: str
    date: str
    time: str

events = []

@app.post("/events")
def add_event(event: Event):
    events.append(event)
    return {"message": "Event added", "event": event}

@app.get("/events")
def get_events():
    return events


# Lancer le serveur avec la commande suivante :
# uvicorn main:app --reload
