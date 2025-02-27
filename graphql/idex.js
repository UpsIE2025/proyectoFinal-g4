const express = require('express');
const { ApolloServer } = require('apollo-server-express');
const cors = require('cors');
const typeDefs = require('./graphql/typeDefs'); // Importa el esquema GraphQL
const resolvers = require('./graphql/resolvers'); // Importa los resolvers


