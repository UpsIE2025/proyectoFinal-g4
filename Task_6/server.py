import grpc
import sys
sys.path.append("grpcgen")
import service_pb2
import service_pb2_grpc
from concurrent import futures
import time

# Almacena los mensajes enviados
historial_mensajes = []
clientes_conectados = {}  # Almacenar clientes conectados con su índice de mensajes

class MessageService(service_pb2_grpc.MessageServiceServicer):
    def SendMessage(self, request, context):
        print(f"Mensaje recibido del producer: {request.messagecom}")
        historial_mensajes.append(request.messagecom)  # Guardamos todos los mensajes

        return service_pb2.MessageResponse(messagecom="Mensaje recibido correctamente")

    def ReceiveMessages(self, request, context):
        global clientes_conectados
        clientes_conectados[context] = len(historial_mensajes)  # Guardar la posición del último mensaje recibido

        try:
            while True:
                ultima_posicion = clientes_conectados[context]
                # Si hay nuevos mensajes, enviarlos al cliente
                while ultima_posicion < len(historial_mensajes):
                    messagecom = historial_mensajes[ultima_posicion]
                    yield service_pb2.MessageResponse(messagecom=messagecom)
                    ultima_posicion += 1  # Avanzar al siguiente mensaje

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

def iniciar_servidor():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MessageServiceServicer_to_server(MessageService(), servidor)
    servidor.add_insecure_port("[::]:50051")
    servidor.start()
    print("Servidor gRPC en ejecución en el puerto 50051...")
    servidor.wait_for_termination()

if __name__ == "__main__":
    iniciar_servidor()

