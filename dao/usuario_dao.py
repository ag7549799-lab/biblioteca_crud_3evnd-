# DAO: Data Access Object
# libro_dao: Objeto de acceso a datos de la tabla libro

from database.conexion import Conexion
from models.usuario import  Usuario 

class UsuarioDAO:

    # SELECT * from usuario
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()        

        cursor.execute("SELECT * FROM vista_usuarios")
        registros = cursor.fetchall()

        usuarios = []
        for registro in registros:
            usuario = Usuario(
                id=registro[0],
                matricula=registro[1],
                nombre=registro[2],
                carrera=registro[3],
                correo=registro[4],
                activo=registro[5]
            )
            usuarios.append(usuario)
        cursor.close()
        conexion.close()
        return usuarios

    def insertar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
        INSERT INTO libro (id, titulo, autor, isbn, disponible)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (libro.id,
             libro.titulo, 
             libro.autor, 
             libro.isbn, 
             libro.disponible)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE libro
        SET titulo = %s, autor = %s, isbn = %s, 
        disponible = %s
        WHERE id = %s
        """
        cursor.execute(
            sql,
            (libro.titulo, 
             libro.autor, 
             libro.isbn, 
             libro.disponible,
             libro.id)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, libro_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            " DELETE FROM libro WHERE id = %s",
            (libro_id,)
            )
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM libro ORDER BY id DESC")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]
    