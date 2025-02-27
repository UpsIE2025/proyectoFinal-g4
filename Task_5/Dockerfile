FROM python:3.9-slim

WORKDIR /code

# Install system dependencies required for psycopg2
RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /code/app

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]