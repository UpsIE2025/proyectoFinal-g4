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
--header 'Authorization: Bearer CUALQUIER_TOKEN_O_NADA' \
--data-raw '{
    "query": "query { saveStudent(input: { id: 1, nombre: \"Luis\", apellido: \"Pérez\", correo: \"juan@example.com\", fecha_nacimiento: \"2000-05-20\", semestre: \"2\", action: \"create\" }) { message status } }"
  }'

---


## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.

