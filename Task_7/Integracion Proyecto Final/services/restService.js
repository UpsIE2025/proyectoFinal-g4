const axios = require("axios");

//prueba real
/*
const callRestService = async (studentData) => {
  try {
    const response = await axios.post(process.env.REST_SERVICE_URL, studentData);

    return { status: response.status, data: response.data };
  } catch (error) {
    console.error("Error en REST:", error.message);
    throw new Error("Error en la API REST");
  }
};
*/

//prueba mock
const callRestService = async (studentData) => {
  console.log("📡 Simulando llamada a REST con:", studentData);

  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("✅ REST responde con 202");
      resolve({ status: 202, data: { message: "Estudiante guardado en REST" } });
    }, 1000);
  });
};

module.exports = { callRestService };
