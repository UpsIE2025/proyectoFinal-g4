require("dotenv").config();
const { ApolloServer, gql } = require("apollo-server");
const authenticate = require("./services/auth");
const { callRestService } = require("./services/restService");
const { callGrpcService } = require("./services/grpcService");

const typeDefs = gql`
  type Query {
    saveStudent(input: StudentInput!): Response
  }

  input StudentInput {
    id: Int
    nombre: String!
    apellido: String!
    carrera: String!
    semestre: Int
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

      const restResponse = await callRestService(input);

      if (restResponse.status === 202) {

        const grpcResponse = await callGrpcService(input);

        return {
          message: `Guardado en REST y gRPC: ${grpcResponse.success}`,
          status: "OK",
        };
      }

      return {
        message: "Guardado solo en REST",
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
