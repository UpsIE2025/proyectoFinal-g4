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
    """
    Consume messages from a Kafka topic and perform actions based on the received events.

    This function connects to a Kafka cluster, subscribes to a specific topic, and consumes messages from it.
    It processes the events received and performs different actions based on the event type and data.

    The function expects the following environment variable to be set:
    - KAFKA_URL: The URL of the Kafka cluster to connect to.

    The function uses the following parameters for consuming messages:
    - topic: The name of the Kafka topic to subscribe to.
    - bootstrap_servers: The list of Kafka broker URLs to bootstrap the connection.
    - auto_offset_reset: The strategy to use when there is no initial offset in Kafka or if the current offset does not exist.
    - enable_auto_commit: Whether to automatically commit the consumed offsets.
    - group_id: The consumer group ID to join.
    - value_deserializer: The deserializer function to use for deserializing the message values.
    - key_deserializer: The deserializer function to use for deserializing the message keys.

    The function processes the received messages and performs the following actions:
    - For events with operation "c" (create) or "u" (update), it parses the date of birth and saves the student data.
    - For events with operation "d" (delete), it deletes the student data based on the ID.

    If the event operation is not recognized, it prints "Another event".

    If any error occurs during the consumption process, it prints the error message.

    Note: This function assumes the existence of the following helper functions:
    - save_student: A function to save the student data.
    - delete_student_id: A function to delete the student data based on the ID.
    """

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
