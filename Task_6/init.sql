CREATE TABLE IF NOT EXISTS estudiante (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL UNIQUE,
    fecha_nacimiento VARCHAR(255),
    semestre VARCHAR(50)
);

