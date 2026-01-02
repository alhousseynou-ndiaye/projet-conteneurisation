FROM python:3.12-slim

RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Crée le dossier de DB et donne les droits à l'utilisateur non-root
RUN mkdir -p /data && chown -R appuser:appuser /data

ENV DB_PATH=/data/app.db

USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
