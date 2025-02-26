import grpc
import sys
sys.path.append("grpcgen")
import service_pb2
import service_pb2_grpc

def ejecutar_cliente():
    channel = grpc.insecure_channel('localhost:50051')
    stub = service_pb2_grpc.MessageServiceStub(channel)

    print("Conectado al servidor. Escuchando mensajes...")
    respuesta_stream = stub.ReceiveMessages(service_pb2.Empty())

    try:
        for respuesta in respuesta_stream:
            print("📩 Mensaje recibido:", respuesta.messagecom)
    except KeyboardInterrupt:
        print("Cliente desconectado.")


if __name__ == "__main__":
    ejecutar_cliente()

