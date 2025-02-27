const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

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

module.exports = { callGrpcService };
