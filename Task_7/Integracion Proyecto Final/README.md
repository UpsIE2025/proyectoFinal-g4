# 📦 INTEGRACION GRAPQL


## 🔧 Configuración y Ejecución

## Ejecutar el proyecto
npm install
npm run start

## Ejecutar docker
docker-compose up --build

---

## 🛠 Endpoints disponibles

### Guardar Estudiante

## Curl
curl --location 'http://localhost:4000/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer TU_TOKEN_JWT' \
--data '{
    "query": "query { saveStudent(input: { id: 1, nombre: \"Juan\", apellido: \"Pérez\", carrera: \"Ingeniería en mecanica\", semestre: 2 }) { message status } }"
  }'

---


## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.

