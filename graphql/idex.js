const express = require('express');
const { ApolloServer } = require('apollo-server-express');
const cors = require('cors');
const typeDefs = require('./graphql/typeDefs'); // Importa el esquema GraphQL
const resolvers = require('./graphql/resolvers'); // Importa los resolvers


const app = express();

app.use(cors());

async function startServer() {
  const server = new ApolloServer({
    typeDefs,
    resolvers
  });

  await server.start();
  server.applyMiddleware({ app });

  const PORT = process.env.PORT || 4000;
  app.listen(PORT, () => {
    console.log(`🚀 Servidor GraphQL corriendo en http://localhost:${PORT}/graphql`);
  });
}

startServer();