# Usa la imagen oficial de Flutter con soporte para Android
FROM cirrusci/flutter:stable

# Establecer directorio de trabajo
WORKDIR /app

# Copiar el código fuente de Flutter
COPY . .

# Instalar dependencias
RUN flutter pub get

# Compilar APK
RUN flutter build apk

# Mostrar el contenido de la carpeta de salida
CMD ["ls", "-l", "build/app/outputs/flutter-apk/"]
