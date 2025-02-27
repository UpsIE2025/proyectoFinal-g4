const { obtenerEstudiante, crearEstudiante, actualizarEstudiante, listarEstudiantes, eliminarEstudiante } = require('../grpc/grpcClient');

const resolvers = {
  Query: {
    obtenerEstudiante: async (_, { id }) => await obtenerEstudiante(id),
    listarEstudiantes: async () => await listarEstudiantes(),
  },
  Mutation: {
    crearEstudiante: async (_, args) => await crearEstudiante(args.nombre, args.apellido, args.correo, args.fecha_nacimiento, args.carrera, args.semestre),
    actualizarEstudiante: async (_, args) => await actualizarEstudiante(args.id, args.nombre, args.apellido, args.correo, args.fecha_nacimiento, args.carrera, args.semestre),
    eliminarEstudiante: async (_, { id }) => await eliminarEstudiante(id),
  }
};

module.exports = resolvers;
