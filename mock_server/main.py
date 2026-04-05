from fastapi import FastAPI
from router import router
from services import get_state, reset

app = FastAPI()

app.include_router(router)

@app.get("/debug/state")
def state():
    return get_state()

@app.post("/debug/reset")
def reset_state():
    return reset()