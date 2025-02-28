#!/bin/sh
set -e

# Esperar 10 segundos para que Kong esté listo...  Esto es importante.
echo "Esperando 10 segundos para que Kong esté listo..."
sleep 10

# Helper function to create entities (use JSON for consistency and GraphQL)
create_entity() {
    local endpoint="$1"
    local data="$2"
    local content_type="${3:-application/json}"  # Default to JSON

    echo "Creating ${endpoint} with data: ${data}"

    curl -v -s -X POST \
        -H "Content-Type: ${content_type}" \
        --data "$data" \
        "http://kong:8001/${endpoint}"
}

# ------------------- Consumer Configuration  (For Key Auth) -------------------

# Create a consumer using JSON
CONSUMER_DATA='{"username": "upsadmin"}'
create_entity "consumers" "$CONSUMER_DATA"

# ------------------- GraphQL Service & Route Configuration -------------------

# Crear el servicio GraphQL
GRAPHQL_SERVICE_DATA='{"name": "graphql-service", "url": "http://graphql_server:4000"}'
create_entity "services" "$GRAPHQL_SERVICE_DATA"

# Crear la ruta GraphQL
GRAPHQL_ROUTE_DATA='{"paths": ["/graphql"], "service": {"name": "graphql-service"}}'
create_entity "services/graphql-service/routes" "$GRAPHQL_ROUTE_DATA" # Changed from "routes"

# ------------------- Key Authentication Plugin for graphql-service  -------------------

# Enable Key Authentication using JSON
KEY_AUTH_PLUGIN_DATA='{"name": "key-auth", "service": {"name": "graphql-service"}}'
create_entity "services/graphql-service/plugins" "$KEY_AUTH_PLUGIN_DATA"


# ------------------- CORS Plugin for graphql-service  -------------------

curl --location 'http://kong:8001/services/graphql-service/plugins' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'name=cors' \
--data-urlencode 'config.origins=*' \
--data-urlencode 'config.methods=POST' \
--data-urlencode 'config.headers=Accept,Authorization,Content-Type,apikey' \
--data-urlencode 'config.exposed_headers=Authorization' \
--data-urlencode 'config.credentials=true' \
--data-urlencode 'config.max_age=3600'



# Install graphql-proxy plugin. VERY IMPORTANT for GraphQL
GRAPHQL_PLUGIN_DATA='{"name": "graphql-proxy", "service": {"name": "graphql-service"}}'
create_entity "services/graphql-service/plugins" "$GRAPHQL_PLUGIN_DATA"


echo "Kong configuration complete."