from flask import Flask, request, jsonify
import grpc
import sys
sys.path.append("grpcgen")
import service_pb2
import service_pb2_grpc

app = Flask(__name__)

channel = grpc.insecure_channel('grpc-server:50051')
stub = service_pb2_grpc.UserServiceStub(channel)

@app.route('/enviar', methods=['POST'])
def enviar_mensaje():
    data = request.get_json()
    message = data
    if not message:
        return jsonify({"error": "Se requiere un mensaje"}), 400

    print(f"Enviando mensaje gRPC: {message}")
    message = service_pb2.UserRequest(
        id=int(data.get("id", 0)),
        nombre=str(data.get("nombre", "")),
        apellido=str(data.get("apellido", "")),
        correo=str(data.get("correo", "")),
        fecha_nacimiento=str(data.get("fecha_nacimiento", "")),
        semestre=str(data.get("semestre", "")),
        action=str(data.get("action", ""))
    )
    stub.SendMessage(message)
    print(f"Mensaje enviado: {message}")

    return jsonify({"menssage": "Mensaje enviado correctamente"}), 200

@app.route('/leer', methods=['GET'])
def leer_mensaje():
    user_id = request.args.get("id")
    if not user_id:
        return jsonify({"error": "Se requiere un ID"}), 400

    print(f"Solicitud de lectura recibida: {user_id}")
    #return jsonify({"menssage": "Solicitud de lectura recibida"}), 200

    try:
        # Realiza la llamada sincrónica al método GetUser
        response = stub.GetUser(service_pb2.UserIdRequest(id=int(user_id)))
        # Convierte la respuesta a diccionario para devolverlo en JSON
        user_data = {
            "id": response.id,
            "nombre": response.nombre,
            "apellido": response.apellido,
            "correo": response.correo,
            "fecha_nacimiento": response.fecha_nacimiento,
            "semestre": response.semestre
        }
        return jsonify(user_data), 200
    except grpc.RpcError as e:
        print(f"Error al realizar la solicitud: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

