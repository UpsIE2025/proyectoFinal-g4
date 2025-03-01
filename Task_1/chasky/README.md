# Proyecto Final G4

## Instrucciones para la Configuración del Proyecto

Para configurar el proyecto, sigue estos pasos:

1. **Clona el repositorio**: Usa Git para clonar el repositorio del proyecto en tu máquina local.

2. **Navega al directorio del proyecto**: Abre una terminal y cambia al directorio del proyecto:
   ```
   cd proyectoFinal-g4
   ```

3. **Instala el SDK de Dart**: Asegúrate de tener el SDK de Dart instalado en tu máquina. Puedes descargarlo desde el sitio web oficial de Dart.

4. **Instala las dependencias**: Ejecuta el siguiente comando para instalar los paquetes requeridos:
   ```
   dart pub get
   ```

5. **Configura el API Gateway**:
   - Abre el archivo `lib/src/environment/environment.dart`.
   - Localiza la variable `API_GATEWAY` y configúrala con tu endpoint de GraphQL. Por ejemplo:
     ```
     static const String API_GATEWAY = 'https://your-graphql-endpoint.com/graphql';
     ```

6. **Ejecuta la aplicación**: Usa el siguiente comando para ejecutar la aplicación:
   ```
   dart run lib/src/main.dart
   ```

7. **Verifica la configuración**: Revisa la consola en busca de errores y asegúrate de que la aplicación se esté ejecutando como se espera.

Siguiendo estos pasos, tendrás el proyecto configurado y listo para usar.