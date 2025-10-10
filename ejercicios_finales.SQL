#MySQL

#ejercicio1

CREATE DATABASE almacen_datos;
USE almacen_datos;

CREATE TABLE empleados (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(100),
    puesto VARCHAR(50),
    salario DECIMAL(10, 2),
    fecha_contratacion DATE
);

#ejercicio2

INSERT INTO empleados (id_empleado, nombre, puesto, salario, fecha_contratacion) VALUES
(1, 'Ana García', 'Gerente', 75000.00, '2020-05-15'),
(2, 'Juan Pérez', 'Desarrollador', 55000.00, '2021-08-20'),
(3, 'María López', 'Analista', 48000.00, '2022-01-10'),
(4, 'Carlos Ruiz', 'Desarrollador', 58000.00, '2020-11-01'),
(5, 'Elena Torres', 'Diseñadora', 50000.00, '2023-03-25');

#ejercicio3


SELECT * FROM empleados;

#ejercicio4

SELECT * FROM empleados WHERE puesto = 'Desarrollador';

SELECT * FROM empleados WHERE fecha_contratacion > '2022-01-01';



#ejercicio5

UPDATE empleados SET puesto = 'Gerente Senior', salario = 85000.00 WHERE id_empleado = 1;

#ejercicio6

DELETE FROM empleados WHERE id_empleado = 5;

#ejercicio7

SELECT * FROM empleados ORDER BY nombre ASC;

SELECT * FROM empleados ORDER BY fecha_contratacion DESC;

#ejercicio8

CREATE TABLE proyectos (
    id_proyecto INT PRIMARY KEY,
    nombre_proyecto VARCHAR(100),
    id_empleado_lider INT,
    FOREIGN KEY (id_empleado_lider) REFERENCES empleados(id_empleado)
);

INSERT INTO proyectos (id_proyecto, nombre_proyecto, id_empleado_lider) VALUES
(101, 'Sistema de Facturación', 2),
(102, 'Migración a la Nube', 1),
(103, 'Aplicación Móvil', 3);

#ejercicio9

SELECT
    e.nombre AS Nombre_Lider,
    p.nombre_proyecto AS Proyecto_Liderado
FROM
    empleados e
INNER JOIN
    proyectos p ON e.id_empleado = p.id_empleado_lider;

#ejercicio10

SELECT
    puesto,
    COUNT(id_empleado) AS Total_Empleados
FROM
    empleados
GROUP BY
    puesto;
