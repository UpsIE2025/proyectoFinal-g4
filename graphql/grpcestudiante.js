const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const path = require("path");

const PROTO_PATH = path.join(__dirname, '/estudiante.proto');

// Cargar el archivo .proto
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
  });

const estudianteProto = grpc.loadPackageDefinition(packageDefinition).estudiante;

// Crear el cliente gRPC
let client;

try {
  client = new estudianteProto.EstudianteGrpcService(
    'localhost:50000', // Dirección del servidor gRPC
    grpc.credentials.createInsecure()
  );
} catch (error) {
  console.error('Error al conectar con gRPC:', error);
}

// Funciones para interactuar con el servicio gRPC
function obtenerEstudiante(id) {
  return new Promise((resolve, reject) => {
    client.ObtenerEstudiante({ id }, (err, response) => {
      if (err) reject(err);
      else resolve(response);
    });
  });
}

function crearEstudiante(nombre, apellido, correo, fecha_nacimiento, carrera, semestre) {
  return new Promise((resolve, reject) => {
    client.CrearEstudiante({ nombre, apellido, correo, fecha_nacimiento, carrera, semestre }, (err, response) => {
      if (err) reject(err);
      else resolve(response);
    });
  });
}

function actualizarEstudiante(id, nombre, apellido, correo, fecha_nacimiento, carrera, semestre) {
  return new Promise((resolve, reject) => {
    client.ActualizarEstudiante({ id, nombre, apellido, correo, fecha_nacimiento, carrera, semestre }, (err, response) => {
      if (err) reject(err);
      else resolve(response);
    });
  });
}

function listarEstudiantes() {
  return new Promise((resolve, reject) => {
    client.ListarEstudiantes({}, (err, response) => {
      if (err) reject(err);
      else resolve(response.estudiantes);
    });
  });
}

function eliminarEstudiante(id) {
  return new Promise((resolve, reject) => {
    client.EliminarEstudiante({ id }, (err, response) => {
      if (err) reject(err);
      else resolve(response);
    });
  });
}

module.exports = {
  obtenerEstudiante,
  crearEstudiante,
  actualizarEstudiante,
  listarEstudiantes,
  eliminarEstudiante
};