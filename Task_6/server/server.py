import grpc
import sys
import uuid, threading
sys.path.append("grpcgen")
import service_pb2
import service_pb2_grpc
from concurrent import futures
import time

# Almacena los mensajes enviados
historial_mensajes = []
clientes_conectados = {}  # Almacenar clientes conectados con su índice de mensajes
pending_requests = {}        # Diccionario: correlation_id -> {"event": threading.Event, "response": UserResponse}


class UserService(service_pb2_grpc.UserServiceServicer):
    def ReceiveMessages(self, request, context):
        #yield service_pb2.ActionMessage(action="create", data=service_pb2.UserRequest(id=1, nombre="Juan", apellido="Perez", correo="juan@example.com", fecha_nacimiento="2000-01-01", semestre="5")) 
        global clientes_conectados
        clientes_conectados[context] = len(historial_mensajes)  # Guardar la posición del último mensaje recibido

        try:
            while True:
                ultima_posicion = clientes_conectados[context]
                # Si hay nuevos mensajes, enviarlos al cliente
                while ultima_posicion < len(historial_mensajes):
                    data = historial_mensajes[ultima_posicion]
                    yield service_pb2.ActionMessage(action=data.action, data=data)        
                    ultima_posicion += 1  # Avanzar al siguiente mensaje
                    #data=service_pb2.UserRequest(id=1, name="", username="", password="")

                # Actualizamos la posición para el cliente
                clientes_conectados[context] = ultima_posicion
                time.sleep(1)  # Evitar consumo alto de CPU

        except grpc.RpcError as e:
            # Si el cliente lanza un error, lo eliminamos del diccionario
            print(f"Cliente desconectado con error: {e}")
            clientes_conectados.pop(context)
        except Exception as e:
            # Excepción genérica para cualquier otro error
            print(f"Error inesperado: {e}")
            clientes_conectados.pop(context)
    
    def SendMessage(self, request, context):
        print(f"Mensaje: {request}")
        print(f"Mensaje recibido del producer: {request.action}")
        if request.action == "read_response":
            print(f"Respuesta recibida del clientmicro: {request.correlation_id}")
            corr_id = request.correlation_id
            if corr_id in pending_requests:
                # Asumimos que request.data contiene la respuesta en formato UserRequest
                user_resp = service_pb2.UserResponse(
                    id=request.id,
                    nombre=request.nombre,
                    apellido=request.apellido,
                    correo=request.correo,
                    fecha_nacimiento=request.fecha_nacimiento,
                    semestre=request.semestre
                )
                pending_requests[corr_id]["response"] = user_resp
                pending_requests[corr_id]["event"].set()
        else:
            historial_mensajes.append(request)  # Guardamos todos los mensajes
        #historial_mensajes.append(service_pb2.ActionMessage(action="create", data=request))
        '''if request.data.action == "read":
            return service_pb2.UserResponse(data="Mensaje recibido correctamente")    
        return service_pb2.MessageResponse(data="Mensaje recibido correctamente 1")'''
        print(f"Fin send message")
        return service_pb2.Empty()
        #return service_pb2.ActionMessage(action="received", data=request)

    def GetUser(self, request, context):
        # Genera un correlation_id
        print(f"Solicitud de lectura recibida: {request.id}")
        correlation_id = str(uuid.uuid4())
        event = threading.Event()
        pending_requests[correlation_id] = {"event": event, "response": None}

        read_msg = service_pb2.UserRequest(id=request.id)
        read_msg.action = "read"
        read_msg.correlation_id = correlation_id

        # Enviar la solicitud de lectura al clientmicro vía el stream de mensajes
        '''read_msg = service_pb2.ActionMessage(
            action="read",
            correlation_id=correlation_id,
            data=service_pb2.UserRequest(id=request.id)  # Sólo enviamos el id
        )'''
        historial_mensajes.append(read_msg)

        # Espera la respuesta (timeout de, por ejemplo, 10 segundos)
        print(f"Esperando respuesta para correlación {correlation_id}")
        if event.wait(timeout=10):
            print(f"Respuesta recibida para correlación {correlation_id}")
            resp = pending_requests[correlation_id]["response"]
            del pending_requests[correlation_id]
            return resp
        else:
            print(f"No se recibió respuesta para correlación {correlation_id}")
            del pending_requests[correlation_id]
            context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
            context.set_details("Timeout esperando respuesta")
            return service_pb2.UserResponse()

def iniciar_servidor():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), servidor)
    servidor.add_insecure_port("[::]:50051")
    servidor.start()
    print("Servidor gRPC en ejecución en el puerto 50051...")
    servidor.wait_for_termination()

if __name__ == "__main__":
    iniciar_servidor()
