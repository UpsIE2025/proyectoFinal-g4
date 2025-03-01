import grpc
import sys
import psycopg2
sys.path.append("grpcgen")
import service_pb2
import service_pb2_grpc
import time
import datetime

# Configuración de la base de datos
DB_CONFIG = {
    "dbname": "change_data_capture",
    "user": "postgres",
    "password": "mypassword",
    "host": "postgres",
    "port": "5432"
}

def connect_db():
    return psycopg2.connect(**DB_CONFIG)

def process_message(message):
    action = message.action.lower()
    data = message.data
    print(f"Received action: {action}")
    print(f"Received action: {data}")

    with connect_db() as conn:
        with conn.cursor() as cursor:
            if action == "create":
                cursor.execute("INSERT INTO estudiantes (nombre, apellido, correo, fecha_nacimiento, semestre) VALUES (%s, %s, %s, %s, %s) RETURNING id", 
                               (data.nombre, data.apellido, data.correo, datetime.datetime.now().date(), data.semestre))
                user_id = cursor.fetchone()[0]
                print(f"User created with ID: {user_id}")
            elif action == "read":
                 # Extrae el correlation_id y el id de usuario
                corr_id = data.correlation_id
                user_id = data.id
                print(f"Procesando read para id {user_id} con correlación {corr_id}")
                cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (user_id,))
                user = cursor.fetchone()
                if user:
                    print(f"User found: {user}")
                    response_msg = service_pb2.UserRequest(
                        id=int(user[0]),
                        nombre=str(user[1]),
                        apellido=str(user[2]),
                        correo=str(user[3]),
                        fecha_nacimiento=str(user[4]),
                        semestre=str(user[5]),
                        action="read_response",
                        correlation_id=corr_id
                    )
                    
                else:
                    print("User not found")
                    response_msg = service_pb2.UserRequest(
                        id=0,
                        nombre="",
                        apellido="",
                        correo="",
                        fecha_nacimiento="",
                        semestre="",
                        action="read_response",
                        correlation_id=corr_id
                    )
                    
                # Envía la respuesta de vuelta al server (como cliente gRPC)
                print(f"Enviando respuesta: {response_msg}")
                channel = grpc.insecure_channel('grpc-server:50051')
                stub = service_pb2_grpc.UserServiceStub(channel)
                stub.SendMessage(response_msg)
                print("Respuesta enviada para correlación", corr_id)
            elif action == "update":
                cursor.execute("UPDATE estudiantes SET nombre = %s, apellido = %s, correo = %s, fecha_nacimiento = %s, semestre = %s WHERE id = %s", 
                               (data.nombre, data.apellido, data.correo, data.fecha_nacimiento, data.semestre, data.id))
                print("User updated successfully")
            elif action == "delete":
                cursor.execute("DELETE FROM estudiantes WHERE id = %s", (data.id,))
                print("User deleted successfully")
            conn.commit()

def listen_for_messages():
    channel = grpc.insecure_channel('grpc-server:50051')
    stub = service_pb2_grpc.UserServiceStub(channel)
    
    print("Listening for messages from gRPC server...")
    for message in stub.ReceiveMessages(service_pb2.Empty()):
        process_message(message)

if __name__ == "__main__":
    listen_for_messages()
