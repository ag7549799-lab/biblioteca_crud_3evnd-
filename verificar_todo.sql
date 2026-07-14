
SELECT * FROM usuarios;


SELECT * FROM libros;


SELECT * FROM prestamos;


SELECT * FROM carrera;

SELECT column_name, data_type, is_nullable 
FROM information_schema.columns 
WHERE table_name = 'carrera';
