# 📦 NestJS + RabbitMQ

Este proyecto es una aplicación construida con **NestJS** que utiliza **RabbitMQ** para la comunicación asíncrona entre servicios.

---

## 🚀 Tecnologías utilizadas

- **NestJS** - Framework para Node.js
- **RabbitMQ** - Sistema de mensajería
- **Docker & Docker Compose** - Para la gestión de contenedores
- **TypeScript** - Lenguaje principal del proyecto

---


## 🔧 Configuración y Ejecución

## Ejecutar un docker con RabbiMQ
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management


## Ejecutar el proyecto NestJS
npm run start

---

## 🛠 Endpoints disponibles

### 📤 Publicar un mensaje en RabbitMQ (Producer)

## Curl
curl --location 'http://localhost:3000/publish' \
--header 'Content-Type: application/json' \
--data '{
    "message": "Hola desde Docker",
    "valid": true
}'

---

### 📥 Consumir mensajes de RabbitMQ (Consumer)
El consumidor escucha automáticamente los mensajes enviados a la cola de RabbitMQ.
Filtro: si valid es true acepta el mensaje caso contrario los deniega.

---


## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.

