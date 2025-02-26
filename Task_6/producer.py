from flask import Flask, request, jsonify
import grpc
import sys
sys.path.append("grpcgen")
import service_pb2
import service_pb2_grpc

app = Flask(__name__)

channel = grpc.insecure_channel('localhost:50051')
stub = service_pb2_grpc.MessageServiceStub(channel)

@app.route('/enviar', methods=['POST'])
def enviar_mensaje():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "Se requiere un mensaje"}), 400

    print(f"Enviando mensaje gRPC: {message}")
    stub.SendMessage(service_pb2.MessageRequest(messagecom=message))

    return jsonify({"menssage": "Mensaje enviado correctamente"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)

