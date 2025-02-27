CREATE TABLE estudiantes (
    id                  SERIAL PRIMARY KEY,
    nombre              VARCHAR(100) NOT NULL,
    apellido            VARCHAR(100) NOT NULL,
    correo              VARCHAR(150) NOT NULL,
    fecha_nacimiento    DATE,
    carrera             VARCHAR(100),
    semestre            INT
);

INSERT INTO estudiantes (nombre, apellido, correo, fecha_nacimiento, carrera, semestre)
VALUES ('Juan', 'Pérez', 'juan.perez@example.com', '2000-05-15', 'Ingeniería Informática', 3);

INSERT INTO estudiantes (nombre, apellido, correo, fecha_nacimiento, carrera, semestre)
VALUES ('María', 'Gómez', 'maria.gomez@example.com', '1999-09-23', 'Medicina', 5);

INSERT INTO estudiantes (nombre, apellido, correo, fecha_nacimiento, carrera, semestre)
VALUES ('Carlos', 'Rodríguez', 'carlos.rodriguez@example.com', '2001-02-10', 'Derecho', 2);

INSERT INTO estudiantes (nombre, apellido, correo, fecha_nacimiento, carrera, semestre)
VALUES ('Ana', 'Fernández', 'ana.fernandez@example.com', '2002-07-30', 'Arquitectura', 1);

INSERT INTO estudiantes (nombre, apellido, correo, fecha_nacimiento, carrera, semestre)
VALUES ('Luis', 'Martínez', 'luis.martinez@example.com', '1998-12-05', 'Administración de Empresas', 6);
