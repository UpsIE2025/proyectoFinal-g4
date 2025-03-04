# Remote Procedure Invocation (RPC) con gRPC en Python

## 1. Introducción
Remote Procedure Call (RPC) es un modelo de comunicación en sistemas distribuidos que permite la ejecución de procedimientos remotos como si fueran funciones locales.

## 2. Comparación entre RPC, REST y gRPC
| Característica  | RPC | REST | gRPC |
|---------------|-----|------|------|
| Protocolo | Propietario / gRPC usa HTTP/2 | HTTP/1.1 | HTTP/2 |
| Formato de datos | Binario | JSON | Protocol Buffers |
| Velocidad | Alta | Media | Muy alta |
| Tipado fuerte | Sí | No | Sí |
| Streaming | Sí (en gRPC) | No | Sí |
| Casos de uso | Servicios internos, alta eficiencia | APIs públicas, interoperabilidad | Sistemas de alto rendimiento, microservicios |

## 3. Ventajas y Desventajas de RPC
### Ventajas
- Mayor eficiencia en la comunicación debido a su formato binario.
- Compatibilidad con múltiples lenguajes de programación.
- Soporte para streaming bidireccional.
- Seguridad y autenticación avanzada.

### Desventajas
- Mayor complejidad en la implementación.
- Puede generar problemas de compatibilidad entre versiones.
- No es ideal para APIs públicas debido a su menor interoperabilidad en comparación con REST.

## 4. Ejemplo de Aplicaciones Empresariales
RPC es ampliamente utilizado en:
- Comunicación entre microservicios en sistemas distribuidos.
- Aplicaciones de alto rendimiento como bases de datos distribuidas.
- Servicios de mensajería y transmisión en tiempo real.
- Plataformas de inteligencia artificial y procesamiento de datos en la nube.

## Ejecución de aplicación
Para Ejecutar y probar la aplicación, se deben seguir los siguientes pasos:
1. Instalar las librerias necesarias a través del siguiente comando:
```sh
pip install --no-cache-dir -r requirements.txt
```   
2. En caso de que no se tengan los scrips (2 archivos .py) dentro de la carpeta grpcgen, ejecutar el siguiente comando para su generación:
```sh
python -m grpc_tools.protoc -I. --python_out=grpcgen --grpc_python_out=grpcgen service.proto
``` 
3. Ejecutar el servidor con el siguiente comando:
```sh
python server.py
```    
4. Ejecutar un cliente con el siguiente comando:
```sh
python client.py
```
Nota: Se pueden ejecutar n clientes con el mismo comando sin problema.
5. Ejecutar el producer para permitir que clientes http puedan consumir el endpoint:
```sh
python producer.py
```
6. Consumir el endpoint con algún cliente http (postman por ejemplo), con los siguientes datos de entrada:
   URL: http://127.0.0.1:5000/enviar
   Método: POST
   Formato: JSON
   Body:
   ```sh
   {
    "message": "¡Mensaje desde postman!"
   }
   ```
   
