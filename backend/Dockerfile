# Utilise une image Python officielle
FROM python:3.11-slim

# Crée un répertoire pour ton app
WORKDIR /app

# Copie le code et les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code
COPY . .

# Expose le port 8080 (utilisé par Fly.io)
EXPOSE 8080

# Commande de lancement de ton app FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
