const axios = require("axios");

const callRestService = async (studentData) => {
  try {
    const response = await axios.post(process.env.REST_SERVICE_URL, studentData);

    return { status: response.status, data: response.data };
  } catch (error) {
    console.error("Error en REST:", error.message);
    throw new Error("Error en la API REST");
  }
};

module.exports = { callRestService };
