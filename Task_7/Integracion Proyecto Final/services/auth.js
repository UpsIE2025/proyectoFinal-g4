const jwt = require("jsonwebtoken");

const authenticate = async (token) => {

  //Prueba mock
  console.log("🔹 Simulando autenticación JWT...");
  return { id: 1, nombre: "Usuario Mock", rol: "admin" };

  //prueba real
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    return decoded;
  } catch (error) {
    throw new Error("Token inválido o expirado");
  }
};

module.exports = authenticate;
