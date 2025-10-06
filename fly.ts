// src/api/crewApi.ts
const BASE_URL = "https://ton-backend-deploy.fly.dev"; // ou render, railway, etc.

export async function kickoffCrew(inputs: Record<string, any>) {
  const res = await fetch(`${BASE_URL}/kickoff`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ inputs }),
  });
  return res.json();
}

export async function getCrewStatus(crewId: string) {
  const res = await fetch(`${BASE_URL}/status/${crewId}`);
  return res.json();
}
