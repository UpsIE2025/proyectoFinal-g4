const axios = require("axios");

const callRestService = async (studentData) => {
  console.log("📡 Intentando conectar a REST en:", process.env.REST_SERVICE_URL);
  try {
    const response = await axios.post(process.env.REST_SERVICE_URL, studentData, {
      headers: { "Content-Type": "application/json" }
    });
    return { status: response.status};
  } catch (error) {
    console.error("Error en REST:", error.message);
    throw new Error("Error en la API REST");
  }
};

module.exports = { callRestService };
