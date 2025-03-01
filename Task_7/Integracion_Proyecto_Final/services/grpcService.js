require("dotenv").config();
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const packageDefinition = protoLoader.loadSync("./service.proto");
const grpcPackage = grpc.loadPackageDefinition(packageDefinition);

const GRPC_HOST = process.env.GRPC_SERVICE_HOST;
console.log("🔗 Conectando a gRPC en:", GRPC_HOST);

const grpcClient = new grpcPackage.service.UserService(
  GRPC_HOST,
  grpc.credentials.createInsecure()
);

const callGrpcService = (studentData) => {
  return new Promise((resolve, reject) => {
    grpcClient.SendMessage(studentData, (error, response) => {
      if (error) {
        console.error("Error en gRPC:", error.message);
        reject(new Error("Error en gRPC"));
      }
      console.log(response);
      resolve(response);
    });
  });
};

module.exports = { callGrpcService };
