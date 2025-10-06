from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, your backend is running!"}

@app.get("/notes")
def get_notes():
    # Later we can connect to a database, for now hardcoded
    return [
        {"id": 1, "title": "First Note", "content": "This is your first note."},
        {"id": 2, "title": "Second Note", "content": "This is your second note."}
    ]
