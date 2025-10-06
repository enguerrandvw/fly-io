from fastapi import FastAPI
from pydantic import BaseModel
from crew_ai import kickoff_crew, get_crew_status

app = FastAPI(title="CrewAI Backend API")

class KickoffInput(BaseModel):
    inputs: dict

@app.get("/")
def root():
    return {"message": "CrewAI Backend is running ✅"}

@app.post("/kickoff")
async def kickoff_endpoint(payload: KickoffInput):
    return await kickoff_crew(payload.inputs)

@app.get("/status/{crew_id}")
async def status_endpoint(crew_id: str):
    return await get_crew_status(crew_id)
