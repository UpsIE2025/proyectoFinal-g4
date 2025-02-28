import json
import os
import threading
from contextlib import asynccontextmanager
from datetime import datetime, timedelta

from fastapi import FastAPI
from kafka import KafkaConsumer

from app.models import Students
from app.repository import save_student, delete_student_id


def consume_kafka():
    kafka_url = os.environ.get('KAFKA_URL')
    topic = "dbserver1.public.estudiantes"
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_url,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="mi-grupo-id",
            value_deserializer=lambda x: json.loads(x.decode("utf-8")) if x else None,
            key_deserializer=lambda x: x.decode("utf-8") if x else None,
        )

        print(f"Esperando mensajes en el tópico {topic}...")

        for msg in consumer:
            print("-----------------------------------")
            event = msg.value
            if not event:
                continue
            payload = event.get("payload", {})

            op = payload.get("op")
            before_data = payload.get("before", None)
            after_data = payload.get("after", None)

            if op in ["c", "u"] and after_data:
                parse_date = datetime(1970, 1, 1) + timedelta(days=after_data['fecha_nacimiento'])
                after_data['fecha_nacimiento'] = parse_date
                student = Students(**after_data)
                save_student(student)
            elif op == "d" and before_data:
                pk = before_data['id']
                delete_student_id(pk)
            else:
                print("Another event")

    except Exception as e:
        print(f"Error en el consumidor: {e.with_traceback(None)}")


@asynccontextmanager
async def lifespan(application: FastAPI):
    kafka_thread = threading.Thread(target=consume_kafka, daemon=True)
    kafka_thread.start()

    yield

    print("Close application...")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def hello(x: float):
    return {"message": "hello world"}
