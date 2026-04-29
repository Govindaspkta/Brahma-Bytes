from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth, task, user

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(task.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Task Manager API is running"}