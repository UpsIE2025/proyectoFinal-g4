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
    semestre: String!
    action: String!
  }

  type Response {
    message: String
    status: String
  }
`;

/**
 * Resolvers for GraphQL queries and mutations.
 *
 * @typedef {Object} Resolvers
 * @property {Object} Query - Resolvers for GraphQL queries.
 * @property {Function} Query.saveStudent - Resolver for saving a student.
 */
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
        semestre: input.semestre,
      };

      const grpcData = {
        ...input,
        correlation_id: correlationId,
        fecha_nacimiento: ""
      };

      
      const restResponse = await callRestService(restData);

      if (restResponse.status === 202) {

        const grpcResponse = await callGrpcService(grpcData);

        return {
          message: `Guardado en REST y gRPC`,
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
