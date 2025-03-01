# Informe Shared Database

Es un sistema que permite multiples usuarios acceder y cambiar la misma base de datos simultaneamente.

## Ventajas
- Almacenamiento centralizado, reduce la complejidad de la sincronización
- Base de datos compartida permite la colaboración y la comunicación
- Evita duplicidad de datos

## Desventajas
- No es viable para bases de datos muy grandes
- Escalibilidad limitada
- Mantenimiento costoso cuanto la base de datos crece
- Una modificación afecta a distintos servicios

## Casos de uso
- Aplicaciones pequeñas
- Sistemas legacy

## Riesgos
- Modificar un esquema en la base de datos conlleva cambios en multiples aplicaciones que dependen del esquema
- Al ser una base de datos compartida con muchos usuarios la seguridad y la concurrencia puede ser compleja
- Riesgo alto de acoplamiento

## Alternativas modernas
### Event-driven 
Comunicación mediante eventos asincronos minimiza el acomplamiento ejemplo Kafka, RabbitMQ, etc.
### Microservicios
Con este enfoque cada dominio de negocio tiene su base de datos

## Repositorio Change Data Capture
https://github.com/UpsIE2025/proyectoFinal-g4/tree/main/Task_5

## Implementación Change Data Capture con Debezium, PostgreSQL, MariaDB, Kafka

Este proyecto configura un **conector Debezium** para capturar cambios en una base de datos **PostgreSQL** y transmitirlos a **Kafka**.

## 📌 Configuración conector Debezium

To register the connector in **Kafka Connect**, send a `POST` request to:

```plaintext
http://localhost:8083/connectors
```

con el siguiente JSON payload:

```json
{
    "name": "postgres-connector",
    "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "tasks.max": "1",
        "database.hostname": "postgres",
        "database.port": "5432",
        "database.user": "postgres",
        "database.password": "mypassword",
        "database.dbname": "change_data_capture",
        "topic.prefix": "dbserver1",
        "plugin.name": "pgoutput",
        "slot.name": "debezium_slot",
        "publication.name": "debezium_pub",
        "publication.autocreate.mode": "all_tables",
        "include.schema.changes": "true"
    }
}
```

## 🚀 Pasos para levantar

### 1️⃣ Inicializar todos los servicios del docker compose

Asegurate de tener instalado `docker` y `docker-compose`. Ejecuta el siguiente comando:

```sh
docker-compose up -d
```

### 2️⃣ Verificación Kafka Connect
Verifica que Kafka Connect este ejecutandose:

```sh
curl http://localhost:8083/connectors
```

### 3️⃣ Registra el conector
Usa postman para enviar a registrar el conector

### 4️⃣ Verifica el registro del conector
Lista todas las conectores registrados:

```sh
curl http://localhost:8083/connectors
```

## 📡 Monitorea los eventos

To view captured events, run:

```sh
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic dbserver1.public.estudiantes --from-beginning
```

---

