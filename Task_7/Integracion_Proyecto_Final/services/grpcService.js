const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

//prueba real
/*
const packageDefinition = protoLoader.loadSync("./service.proto");
const grpcPackage = grpc.loadPackageDefinition(packageDefinition);

const grpcClient = new grpcPackage.MicroService(
  process.env.GRPC_SERVICE_HOST,
  grpc.credentials.createInsecure()
);

const callGrpcService = (studentData) => {
  return new Promise((resolve, reject) => {
    grpcClient.saveStudent(studentData, (error, response) => {
      if (error) {
        console.error("Error en gRPC:", error.message);
        reject(new Error("Error en gRPC"));
      }
      resolve(response);
    });
  });
};
*/

//prueba mock
const callGrpcService = async (studentData) => {
  console.log("📡 Simulando llamada a gRPC con:", studentData);

  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("✅ gRPC responde con success=true");
      resolve({ success: true });
    }, 1000);
  });
};

module.exports = { callGrpcService };
