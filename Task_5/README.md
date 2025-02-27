# Change Data Capture with Debezium and PostgreSQL

This project sets up a **Debezium connector** to capture changes in a **PostgreSQL** database and stream them to **Kafka**.

## 📌 Connector Configuration

To register the connector in **Kafka Connect**, send a `POST` request to:

```plaintext
http://localhost:8083/connectors
```

with the following JSON payload:

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

## 🚀 Setup Steps

### 1️⃣ Start All Services with Docker Compose

Ensure you have `docker` and `docker-compose` installed. Then, create a `docker-compose.yml` file with the following content:

Run the following command to start all services:

```sh
docker-compose up -d
```

### 2️⃣ Check Kafka Connect
Verify that Kafka Connect is running:

```sh
curl http://localhost:8083/connectors
```

### 3️⃣ Register the Connector
Execute:

```sh
curl -X POST -H "Content-Type: application/json" \
--data '@connector-config.json' \
http://localhost:8083/connectors
```

Or use Postman to send the `POST` request.

### 4️⃣ Validate Registration
List active connectors:

```sh
curl http://localhost:8083/connectors
```

## 📡 Monitoring Kafka Events

To view captured events, run:

```sh
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic dbserver1.public.estudiantes --from-beginning
```

---

