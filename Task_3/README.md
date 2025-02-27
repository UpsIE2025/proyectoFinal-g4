# Integración con Apache Kafka

## 1. Introducción
Apache Kafka es una plataforma de mensajería distribuida orientada a eventos. Permite la ingesta, almacenamiento y procesamiento de grandes volúmenes de datos en tiempo real con alta disponibilidad y tolerancia a fallos. Su arquitectura basada en logs distribuidos lo hace ideal para sistemas de streaming de datos.

## 2. Arquitectura y Componentes Clave
Kafka se compone de los siguientes elementos:

### 2.1 Producer
Los productores son aplicaciones que envían mensajes a Kafka. Publican datos en "topics" específicos para ser consumidos por los consumidores.

### 2.2 Broker
Los brokers son los servidores que almacenan los datos y gestionan la distribución de mensajes. Un clúster de Kafka suele tener múltiples brokers para garantizar alta disponibilidad.

### 2.3 Consumer
Los consumidores leen datos de los topics. Pueden suscribirse a un topic y procesar los mensajes en tiempo real o en lotes.

### 2.4 Topic y Partitions
- **Topic**: Categoría donde se publican los mensajes.
- **Partition**: Los topics pueden dividirse en particiones para paralelizar la lectura y escritura, mejorando el rendimiento y la escalabilidad.

## 3. Casos de Uso en Integración Empresarial
Kafka es ampliamente utilizado en distintos escenarios empresariales:
- **Procesamiento de datos en tiempo real**: Seguimiento de eventos en plataformas de comercio electrónico.
- **Microservicios**: Comunicación asincrónica entre servicios.
- **Monitorización y logging**: Agregación de logs de diferentes sistemas para análisis.

## 4. Comparación con Otras Tecnologías de Mensajería
| Característica  | Apache Kafka | RabbitMQ |
|-----------------|-------------|----------|
| Modelo | Basado en logs distribuidos | Basado en colas |
| Enfoque | Streaming de eventos | Mensajería tradicional |
| Persistencia | Alto rendimiento y retención prolongada | Menor retención de mensajes |
| Escalabilidad | Alta, basada en particiones | Limitada por colas |
| Casos de uso | Análisis de datos, Big Data | Comunicación entre microservicios |


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



