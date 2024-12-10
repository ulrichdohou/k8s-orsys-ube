FROM python:3.11-slim

WORKDIR /src

# Copier les requirements et installer les dépendances
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Créer le package app
RUN mkdir app

# Copier les fichiers Python dans le package app
COPY app/*.py app/

# Créer un __init__.py vide
RUN touch app/__init__.py

# Ajouter des logs et le mode debug
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/src

# Commande pour démarrer l'application
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]