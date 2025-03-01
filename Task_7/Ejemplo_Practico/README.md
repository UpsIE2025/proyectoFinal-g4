# Patrón Filtro
En la actualidad, los sistemas de software requieren manejar grandes volúmenes de datos 
y comunicarse de manera eficiente. Para lograrlo, se emplean patrones de integración que 
optimizan la forma en que los datos son procesados. Uno de estos patrones es el Filter 
Pattern, que permite seleccionar y procesar solo los mensajes relevantes dentro de un 
flujo de integración (Hohpe & Woolf, 2003). 

Este informe explora el uso del patrón Filtro en los sistemas de integración, explicando 
su funcionamiento y aplicaciones en tecnologías como Apache Camel, Spring 
Integration y Node.js con Express.js Middleware o NestJS. La finalidad es 
comprender cómo estos sistemas manejan la filtración de datos para mejorar la eficiencia 
en la comunicación entre servicios. 

El Filter Pattern es un patrón de diseño que permite procesar únicamente los datos que 
cumplen con criterios específicos, descartando el resto. En los sistemas de integración, su 
propósito principal es mejorar la eficiencia del procesamiento de mensajes al evitar que 
información innecesaria afecte el rendimiento del sistema (Hohpe & Woolf, 2003). 

Este patrón es ampliamente utilizado en arquitecturas basadas en eventos y sistemas de 
mensajería, como Apache Kafka, RabbitMQ y Redis Streams, donde los mensajes 
pueden pasar por distintos filtros antes de llegar a su destino. Los filtros pueden 
configurarse para eliminar mensajes duplicados, verificar la validez de los datos o 
descartar información no relevante para ciertos consumidores.

Por ejemplo, en un sistema de procesamiento de pagos, un filtro podría permitir el paso 
solo de transacciones superiores a un monto determinado o aquellas que provengan de 
usuarios verificados. Esto evita la sobrecarga en los servicios que procesan las 
transacciones y mejora la seguridad del sistema. 

El Filter Pattern es una implementación común en middleware de integración, 
permitiendo la validación, transformación y enrutamiento de mensajes de manera 
eficiente. Además, su aplicación es clave en arquitecturas orientadas a microservicios, 
donde cada servicio debe recibir únicamente la información necesaria para su operación.

Los sistemas de integración modernos implementan el Filter Pattern para optimizar la 
gestión de datos. Algunas tecnologías que incorporan este patrón son: 

- Apache Camel: Un framework de integración que permite definir filtros dentro 
de sus rutas de procesamiento. Por ejemplo, en una arquitectura basada en Kafka, 
se puede establecer un filtro que descarte mensajes que no contengan ciertos 
atributos necesarios para el procesamiento (Apache Software Foundation, s.f.).

- Spring Integration: Un módulo de Spring que permite aplicar filtros a los 
mensajes en su flujo de integración. Se pueden definir reglas de validación y 
transformación antes de que los datos sean consumidos por otros servicios 
(Pivotal Software, s.f.).

- Node.js con Express Middleware o NestJS: En aplicaciones basadas en Node.js, 
los filtros se implementan a través de middlewares que interceptan las solicitudes 
y validan su contenido antes de ser procesadas. Esto es útil para filtrar solicitudes 
en APIs REST o sistemas de mensajería basados en WebSockets (Node.js 
Foundation, s.f.). 

El patrón filtro se puede combinar con otras técnicas de integración como la 
transformación de datos, el enrutamiento de mensajes y la agregación de eventos, 
permitiendo un flujo más eficiente y organizado en arquitecturas distribuidas. 
Cada una de estas tecnologías implementa el concepto de filtros de manera distinta, pero 
todas buscan el mismo objetivo: optimizar el flujo de mensajes en los sistemas de 
integración. 

Apache Camel utiliza una estructura basada en rutas, donde los filtros pueden agregarse 
como pasos intermedios en la transmisión de mensajes. Permite definir condiciones 
avanzadas mediante expresiones como XPath, JSONPath o Simple Expression 
Language (SPEL), asegurando que solo ciertos mensajes pasen a la siguiente etapa del 
flujo (Apache Software Foundation, s.f.). 

Spring Integration, por otro lado, proporciona un enfoque más orientado a eventos. Los 
filtros en este framework son parte del pipeline de procesamiento y pueden configurarse 
para validar mensajes antes de enviarlos a otros servicios. Se integran fácilmente con 
Spring Boot, lo que facilita su uso en aplicaciones empresariales (Pivotal Software, s.f.). 

En el caso de Node.js con Express Middleware o NestJS, los filtros se implementan 
como middlewares que se ejecutan antes de que una solicitud llegue a su controlador final. 
Esto permite aplicar validaciones, autenticación y transformación de datos de manera 
sencilla, haciendo que estos frameworks sean una opción ideal para construir APIs REST 
con filtrado dinámico (Node.js Foundation, s.f.). 

Aunque Apache Camel y Spring Integration están más orientados a sistemas 
empresariales con altos volúmenes de datos, Node.js ofrece una solución ligera y flexible 
para aplicaciones modernas basadas en microservicios y API-first.

## Conclusión 

El uso de filtros en la integración de sistemas permite optimizar el procesamiento de 
mensajes, asegurando que solo la información relevante llegue a los consumidores 
adecuados. Tecnologías como Apache Camel, Spring Integration y Node.js 
proporcionan distintas formas de implementar este patrón, dependiendo del contexto y 
las necesidades del sistema. 

Comprender y aplicar el Filter Pattern en arquitecturas de integración no solo mejora la 
eficiencia y la escalabilidad, sino que también permite construir sistemas más robustos y 
adaptables a entornos de alta demanda. En el desarrollo de aplicaciones modernas, el uso 
de filtros es clave para garantizar una comunicación eficaz entre servicios y evitar el 
procesamiento innecesario de datos.

## Bibliografía.

- Apache Software Foundation. (s.f.). Apache Camel Documentation. Recuperado 
de https://camel.apache.org/docs/

- Hohpe, G., & Woolf, B. (2003). Enterprise Integration Patterns: Designing, 
Building, and Deploying Messaging Solutions. Addison-Wesley. Recuperado de 
https://www.enterpriseintegrationpatterns.com/

- Node.js Foundation. (s.f.). Node.js v14.x Documentation. Recuperado de 
https://nodejs.org/en/docs/

- Pivotal Software. (s.f.). Spring Integration Reference Manual. Recuperado de 
https://docs.spring.io/spring-integration/reference/

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
npm install
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

