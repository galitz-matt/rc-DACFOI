FROM python:3.12-slim

WORKDIR /app

COPY . /app/backend

RUN pip install --no-cache-dir -r backend/requirements.txt

EXPOSE 5000

CMD ["python", "-m", "backend.app"]