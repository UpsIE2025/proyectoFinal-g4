const { gql } = require('apollo-server-express');

const typeDefs = gql`
  type Estudiante {
    id: ID!
    nombre: String!
    apellido: String!
    correo: String!
    fecha_nacimiento: String
    carrera: String
    semestre: Int
  }

  type Query {
    obtenerEstudiante(id: ID!): Estudiante
    listarEstudiantes: [Estudiante]
  }

  type Mutation {
    crearEstudiante(nombre: String!, apellido: String!, correo: String!, fecha_nacimiento: String, carrera: String, semestre: Int): Estudiante
    actualizarEstudiante(id: ID!, nombre: String, apellido: String, correo: String, fecha_nacimiento: String, carrera: String, semestre: Int): Estudiante
    eliminarEstudiante(id: ID!): String
  }
`;

module.exports = typeDefs;
