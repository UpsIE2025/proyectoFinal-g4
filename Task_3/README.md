# Configuración y Ejecución del Proyecto Kafka con Quarkus

Este documento describe los pasos necesarios para configurar y ejecutar un entorno basado en Apache Kafka y Quarkus, incluyendo un productor y un consumidor.

## Prerrequisitos
- Docker y Docker Compose instalados.
- Java 21 y Maven para ejecutar los proyectos de Quarkus.
- Postman para probar la API.

## Pasos para la Ejecución

### 1. Levantar los contenedores con Docker Compose
Ejecuta el siguiente comando para iniciar los servicios necesarios, incluyendo Kafka:

```sh
docker compose up -d
```

### 2. Acceder al contenedor de Kafka
Ejecuta el siguiente comando para ingresar al contenedor:

```sh
docker exec -it kafka bash
```

### 3. Crear un topic en Kafka
Dentro del contenedor de Kafka, ejecuta el siguiente comando para crear un topic llamado `grupo4-topic`:

```sh
kafka-topics --create --topic grupo4-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### 4. Verificar la creación del topic
Ejecuta el siguiente comando para listar los topics y asegurarte de que `grupo4-topic` se haya creado correctamente:

```sh
kafka-topics --list --bootstrap-server localhost:9092
```

### 5. Levantar los proyectos de Producer y Consumer en Quarkus
Para ejecutar los servicios de productor y consumidor desarrollados en Quarkus, accede a cada proyecto y ejecuta el siguiente comando:

```sh
./mvnw quarkus:dev
```

Repite este paso para ambos proyectos (Producer y Consumer).

### 6. Probar con Postman
Importa la colección de Postman proporcionada y utiliza las solicitudes preconfiguradas para probar la comunicación entre el Producer y el Consumer a través de Kafka.

## Notas Adicionales
- Puedes detener los contenedores cuando termines con el siguiente comando:

```sh
docker compose down
```

---



