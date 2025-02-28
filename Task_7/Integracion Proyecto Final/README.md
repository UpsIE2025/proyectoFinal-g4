# 📦 INTEGRACION GRAPQL


## 🔧 Configuración y Ejecución

## Ejecutar el proyecto
npm install
npm run start

---

## 🛠 Endpoints disponibles

### Guardar Estudiante

## Curl
curl --location 'http://localhost:4000/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer TU_TOKEN_JWT' \
--data-raw '{
    "query": "query { saveStudent(input: { nombre: \"Juan\", apellido: \"Pérez\", correo: \"juan.perez@example.com\", fecha_nacimiento: \"2000-05-20\", carrera: \"Ingeniería en Software\", semestre: 5 }) { message status } }"
  }'

---


## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.

