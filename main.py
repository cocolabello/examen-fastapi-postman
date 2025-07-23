from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Lancer le serveur avec la commande suivante :
# uvicorn main:app --reload
