
# Pasos previos

 1. Instala docker-compose.yml.
 2. Valida que en la ruta exista el servicio msc-productor
 3. Ejecutar docker-compose up -d


# Sección para crear y configurar un servicio en Kong
Este documento explica los pasos necesarios para crear un servicio en Kong, configurar rutas, instalar un plugin de autenticación y probar la funcionalidad del servicio.

## 1. Crear un servicio en Kong

Primero, debemos crear un servicio que apunte a nuestro backend.

curl --location 'http://localhost:8001/services/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'name=msc-productor-service' \
--data-urlencode 'url=http://msc-productor:8080'    

URL de destino: http://msc-productor:8080 es la URL de nuestro servicio backend.
Nombre del servicio: msc-productor-service es el nombre que asignamos a este servicio.



## 2. Crear una ruta para el servicio

A continuación, creamos una ruta que se usará para enrutar las solicitudes a nuestro servicio.


curl --location 'http://localhost:8001/services/msc-productor-service/routes' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'paths%5B%5D=/redis/guardar'

Ruta definida: /redis/guardar es el endpoint que se utilizará para acceder al servicio.


## 3. Desactivar strip_path

Por defecto, Kong elimina (con `strip_path: true`) la parte de la URL definida en `paths[]` antes de enviar la solicitud al backend. Esto puede causar problemas si el backend no está configurado para manejar solicitudes sin esa parte de la ruta.

Para resolver esto, cambiamos `strip_path` a `false`.


curl --location --request PATCH 'http://localhost:8001/routes/37a1f035-3010-426c-af84-64ba9ae9d98d' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'strip_path=false'


## 4. Instalar el plugin de autenticación
Para agregar seguridad al servicio, instalamos el plugin de autenticación basado en clave API.

curl --location 'http://localhost:8001/services/msc-productor-service/plugins' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'name=key-auth'


## 5. Crear un consumidor
Ahora, debemos crear un consumidor que será el usuario que autentique las solicitudes a nuestro servicio.

curl --location 'http://localhost:8001/consumers' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=upsadmin'
•	Nombre del consumidor: upsadmin es el nombre del consumidor.


## 6. Probar la funcionalidad del servicio con el token generado
Una vez configurado todo, probamos el servicio enviando una solicitud con el token de autenticación.

curl --location --request POST 'http://localhost:8000/redis/guardar?clave=mensaje&valor=HolaFunciona' \
--header 'apikey: 4pfeJNKHGqd00v6kLNpMKVSqqRqlTvQB'
•	URL de prueba: http://localhost:8000/redis/guardar?clave=mensaje&valor=HolaFunciona es la URL a la que se enviará la solicitud.
•	Token de API: 4pfeJNKHGqd00v6kLNpMKVSqqRqlTvQB es el token generado para autenticar la solicitud.
