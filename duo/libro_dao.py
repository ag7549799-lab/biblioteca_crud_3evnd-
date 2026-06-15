# DAO: Data Access Object 
# Es una clase que se encarga de acceder a la base de datos y realizar las operaciones
# a la base de datos y realizar las operaciones 

from database.conexion import Conexion
from models.libro import Libro 

class LibroDAO:
    
    def obtener_libros(self):
        conexion = Conexion.obtener_conexion()  
        cursor = conexion.cursor()
        
        # Ejecuta la consulta (eliminamos la duplicada y el espacio en blanco)
        cursor.execute("SELECT * FROM libro")
        
        # Obtiene los resultados
        registros = cursor.fetchall()
        
        # Crear una lista de clase de libro
        libros_objetos = []
        for registro in registros:
            # Aquí desestructuras las columnas de tu tabla libros. 
            
            libro = Libro(registro[0], registro[1], registro[2]) 
            libros_objetos.append(libro)
            
        # Cerrar la conexion 
        cursor.close()
        conexion.close()
        return libro
        
        def insertar(self,libro):
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            sql = """"
        INSERT INTO libro(titulo, autor, isbn, disponible )
        VALUES ($s, %s, $s, %s)
        """
        cursor.execute(sql,(
        libro.titulo,
        libro.autor,
        libro.isbn,
        libro.disponible
    ))
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, libro):
        conexion = Conexion.obtener_conexion()+
    cursos = conexion.cursor()

    sql= """
            UPDATE libro:
            SET titulo = %s, autor=%x,
            isb=%s, disponible=%s
            WHERE id = %s
    """
    
    cursor.execute(sql, (
    libro'titulo',
    libro'autor',
    libro'isbn',
    libro'disponible',
    libro'id'
))


    def eliminar(self, id):
    conexion = Conexion.obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libro WHERE id = %s", (id,))
    
    conexion.commit()
    cursor.close()
    conexion.close()  