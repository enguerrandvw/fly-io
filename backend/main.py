from fastapi import FastAPI
from pydantic import BaseModel
from crew_ai import kickoff_crew, get_crew_status

app = FastAPI()

class KickoffInput(BaseModel):
    inputs: dict

@app.post("/kickoff")
async def kickoff(payload: KickoffInput):
    return await kickoff_crew(payload.inputs)

@app.get("/status/{crew_id}")
async def status(crew_id: str):
    return await get_crew_status(crew_id)
