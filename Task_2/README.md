# Kong Gateway - Guía de Instalación y Configuración

Este documento proporciona instrucciones sobre cómo instalar y configurar Kong Gateway usando Docker Compose, basándose en los archivos `docker-compose.yml` y `setup_kong.sh` proporcionados.

## Requisitos Previos

*   Docker: Asegúrate de que Docker esté instalado en tu sistema. Puedes descargarlo desde el [sitio web oficial de Docker](https://www.docker.com/get-started).
*   Docker Compose: Asegúrate de que Docker Compose también esté instalado. A menudo viene incluido con Docker Desktop. Si no, puedes instalarlo por separado desde la [documentación de Docker](https://docs.docker.com/compose/install/).
*   Una comprensión básica de Docker y Docker Compose.

## Pasos de Instalación

1.  **Clona el Repositorio (o Crea los Archivos Necesarios):**

    Si tienes un repositorio con los archivos `docker-compose.yml` y `setup_kong.sh`, clónalo. De lo contrario, crea estos archivos en un directorio en tu sistema.

    ```bash
    # Ejemplo asumiendo que tienes un repositorio
    git clone <url_de_tu_repositorio>
    cd <directorio_de_tu_repositorio>
    ```

2.  **Crea el Script `setup_kong.sh`:**

    Crea un archivo llamado `setup_kong.sh` en el mismo directorio que tu archivo `docker-compose.yml`.

3.  **Crea el Archivo `docker-compose.yml`:**

    Crea un archivo llamado `docker-compose.yml` en el mismo directorio que tu archivo `setup_kong.sh`. 

4.  **Inicia la Pila de Kong:**

    Abre tu terminal, navega al directorio que contiene el archivo `docker-compose.yml` y ejecuta el siguiente comando:

    ```bash
    docker-compose up -d
    ```

    Este comando iniciará la pila de Kong Gateway en modo desasociado (en segundo plano).

5.  **Verifica la Instalación:**

    Después de que los contenedores estén en ejecución, puedes verificar la instalación accediendo a las siguientes URLs en tu navegador:

    *   **Kong Admin API:** `http://localhost:8001` (o `https://localhost:8444` para SSL)
    *   **Kong Admin UI:** `http://localhost:8002`
    *   **Kong Proxy:** `http://localhost:8000` (o `https://localhost:8443` para SSL)

    También puedes verificar los logs de los contenedores en busca de errores:

    ```bash
    docker-compose logs -f
    ```

## Configuración

El script `setup_kong.sh` configura automáticamente lo siguiente:

*   **Consumidor:** Crea un consumidor con el nombre de usuario `upsadmin`.
*   **Servicio GraphQL:** Crea un servicio llamado `graphql-service` que apunta a `http://graphql_server:4000`. **Importante:** Necesitarás un servidor GraphQL ejecutándose en esta dirección (o ajustar la URL en el script `setup_kong.sh` en consecuencia). Si no tienes uno, recibirás errores cuando Kong intente hacer proxy a él.
*   **Ruta GraphQL:** Crea una ruta para el `graphql-service` que escucha en la ruta `/graphql`.
*   **Plugin de Autenticación por Clave (Key Auth):** Habilita el plugin `key-auth` para el `graphql-service`. Esto requiere que los clientes proporcionen una clave API para acceder al endpoint GraphQL.  Por defecto, Kong buscará la clave en la cabecera `apikey` o como un parámetro.
*   **Plugin CORS:** Habilita el plugin `cors` para el `graphql-service` para permitir solicitudes entre orígenes (cross-origin).
*   **Autenticación por Clave API:** El plugin `key-auth` está habilitado. Necesitarás crear una clave para el consumidor `upsadmin` para acceder al endpoint GraphQL. Puedes hacer esto usando la API de administración de Kong:

    ```bash
    curl -X POST http://localhost:8001/consumers/upsadmin/key-auth
    ```

    Esto devolverá una respuesta JSON que contiene la clave API generada. Incluye esta clave en la cabecera `apikey` o en el parámetro de consulta de tus solicitudes al endpoint `/graphql` (por ejemplo, `curl -H "apikey: <tu_clave_api>" http://localhost:8000/graphql`).

*   **Personalización:** Puedes personalizar la configuración aún más modificando el script `setup_kong.sh`. Por ejemplo, puedes agregar más consumidores, servicios, rutas o plugins.

*   **Persistencia de Postgres:** El volumen `kong-data` asegura que los datos de configuración de Kong se persistan incluso si se reinicia el contenedor de Kong. Si quieres comenzar con una instancia de Kong nueva, puedes eliminar este volumen.

*   **Comprobaciones de Salud (Health Checks):** Las secciones `healthcheck` en el archivo `docker-compose.yml` aseguran que los contenedores estén saludables antes de que se consideren listos. Esto ayuda a prevenir problemas con Kong Gateway.

## Resolución de Problemas

*   **Problemas al Iniciar los Contenedores:** Si los contenedores no se inician, revisa los logs en busca de errores. Los problemas comunes incluyen problemas de conexión a la base de datos o errores de configuración de red.
*   **Acceso a la API de Administración de Kong:** Si no puedes acceder a la API de administración de Kong, asegúrate de que el contenedor de Kong esté en ejecución y de que tu firewall no esté bloqueando el acceso a los puertos 8001 o 8444.
*   **Fallo en las Solicitudes GraphQL:** Si las solicitudes GraphQL están fallando, asegúrate de que la dirección de `graphql-server` sea correcta, de que el plugin `graphql-proxy` esté habilitado y de que estés proporcionando una clave API válida (si `key-auth` está habilitado). Revisa los logs de Kong para obtener mensajes de error más específicos. También, asegúrate de que CORS esté configurado correctamente si estás haciendo solicitudes desde un navegador.

## Información Adicional

*   **Documentación de Kong:** [https://docs.konghq.com/](https://docs.konghq.com/)
*   **Documentación de Docker:** [https://docs.docker.com/](https://docs.docker.com/)
*   **Documentación de Docker Compose:** [https://docs.docker.com/compose/](https://docs.docker.com/compose/)