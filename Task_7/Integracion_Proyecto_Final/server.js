require("dotenv").config();
const { ApolloServer, gql } = require("apollo-server");
const authenticate = require("./services/auth");
const { callRestService } = require("./services/restService");
const { callGrpcService } = require("./services/grpcService");
const { v4: uuidv4 } = require("uuid");

const typeDefs = gql`
  type Query {
    saveStudent(input: StudentInput!): Response
  }

  input StudentInput {
    id: Int
    nombre: String!
    apellido: String!
    correo: String!
    carrera: String!
    semestre: String!
  }

  type Response {
    message: String
    status: String
  }
`;

const resolvers = {
  Query: {
    saveStudent: async (_, { input }, { token }) => {
      
      const user = await authenticate(token);
      const correlationId = uuidv4();

      const restData = {
        id: input.id,
        nombre: input.nombre,
        apellido: input.apellido,
        carrera: input.carrera,
        semestre: parseInt(input.semestre, 10)
      };

      const grpcData = {
        id: input.id,
        nombre: input.nombre,
        apellido: input.apellido,
        correo: input.correo,
        fecha_nacimiento: "",
        semestre: parseInt(input.semestre, 10),
        action: "create",
        correlation_id: correlationId
      };

      
      const restResponse = await callRestService(restData);

      if (restResponse.status === 202) {

        const grpcResponse = await callGrpcService(grpcData);

        return {
          message: `Guardado en REST y gRPC: ${grpcResponse.status}`,
          status: "OK",
        };
      }

      return {
        message: `Guardado solo en REST: ${restResponse.status}`,
        status: "OK",
      };
    },
  },
};

const server = new ApolloServer({
  typeDefs,
  resolvers,
  context: ({ req }) => {
    const token = req.headers.authorization || "";
    return { token };
  },
});

server.listen().then(({ url }) => {
  console.log(`Servidor GraphQL listo en ${url}`);
});
