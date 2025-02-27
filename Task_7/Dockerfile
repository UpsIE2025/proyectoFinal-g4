# 1. Imagen base para NestJS con Node.js
FROM node:20 AS builder

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar los archivos del proyecto
COPY package*.json ./
RUN npm install

# 4. Copiar el resto del código
COPY . .

# 5. Compilar TypeScript
RUN npm run build

# 6. Imagen final para producción
FROM node:20 AS runtime

WORKDIR /app

# 7. Copiar solo la carpeta `dist` y `node_modules` desde el builder
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules

# 8. Exponer el puerto 3000 (donde correrá NestJS)
EXPOSE 3000

# 9. Comando para iniciar la aplicación
CMD ["node", "dist/main.js"]
