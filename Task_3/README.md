# Integración con Apache Kafka

## 1. Introducción
Apache Kafka es una plataforma de mensajería distribuida orientada a eventos. Permite la ingesta, almacenamiento y procesamiento de grandes volúmenes de datos en tiempo real con alta disponibilidad y tolerancia a fallos. Su arquitectura basada en logs distribuidos lo hace ideal para sistemas de streaming de datos.

## 2. Funcionamiento, Arquitectura y Componentes Clave

### 2.1 ¿Cómo funciona Apache Kafka?

### 2.1.1 Producción y Publicación de Mensajes

Los productores (Producers) generan datos y los envían a topics dentro del sistema de Kafka. Estos mensajes pueden contener cualquier tipo de información, como eventos de usuario, registros de logs o transacciones financieras.

    1. El productor se conecta a Kafka
    2. Envía datos a un topic
    3. Kafka distribuye el mensaje en una de las particiones del topic.

### 2.1.2 Almacenamiento y Distribución

Kafka almacena los mensajes en brokers, que forman un clúster. Cada topic se divide en particiones, y cada partición puede tener múltiples réplicas para asegurar la tolerancia a fallos.

    1. Cada mensaje es asignado a una partición, según un esquema de balanceo de carga o clave de partición.

    2. Las particiones permiten que los consumidores procesen mensajes en paralelo.

    3. Kafka almacena los mensajes en disco, permitiendo su lectura incluso si un consumidor se retrasa.

### 2.1.3 Consumo de Mensajes

Los consumidores (Consumers) leen mensajes de los topics de Kafka. Para manejar grandes volúmenes de datos de manera eficiente, se organizan en grupos de consumidores (Consumer Groups).

    1. Un consumidor se suscribe a un topic.

    2. Kafka asigna particiones a los consumidores dentro de un Consumer Group.

    3. Cada consumidor lee los mensajes de su partición asignada.

    4. Kafka mantiene un offset para recordar hasta dónde un consumidor ha leído.

### 2.1.4 Garantía de Entrega

Kafka garantiza diferentes niveles de entrega de mensajes:

    1. At most once (como máximo una vez): puede haber pérdida de mensajes si el consumidor falla.

    2. At keast once(al menos una vez): el mensaje se puede procesar más de una vez en caso de reintento.
    
    3. Exactly once(exactamente una vez): evita la duplicación con una gestión de transacciones avanzada.

### 2.1.5 Coordinación y Administración

Kafka usa Zookeeper para gestionar la configuración del clúster, la elección de líderes y la sincronización entre nodos.

    1. Zookeeper mantiene información sobre los brokers activos.

    2. Gestiona la elección del líder para cada partición.

    3. Almacena metadatos de los consumidores.

### 2.1.6 Casos de uso

![Top casos de uso](res/Use_Case.gif)




Kafka se compone de los siguientes elementos:

### 2.2 Producer
Los productores son aplicaciones que envían mensajes a Kafka. Publican datos en "topics" específicos para ser consumidos por los consumidores.

### 2.3 Broker
Los brokers son los servidores que almacenan los datos y gestionan la distribución de mensajes. Un clúster de Kafka suele tener múltiples brokers para garantizar alta disponibilidad.

### 2.4 Consumer
Los consumidores leen datos de los topics. Pueden suscribirse a un topic y procesar los mensajes en tiempo real o en lotes.

### 2.5 Topic y Partitions
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



