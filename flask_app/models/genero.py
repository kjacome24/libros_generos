from flask_app.config.mysqlconnection import connectToMySQL ###Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos
#####aqui debes importar otras clases en caso de que sea necesario
from flask_app.models.libro import Libro

class Genero:
    db_schema = 'libros_genero' ## Cambiar la BD a la que estamos apuntando
    def __init__(self,data):
# Agregar el los  atributos que vienen de la Base de datos
        self.id = data['id'] 
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.libros = []

    @classmethod
    def get_all(cls):
        query = "select * from generos;" ###cambiar la tabla a la que apuntamos.
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        generos = [] ###Cambiar el nombre del arreglo para algo que represente la tabla
        for genero in resultados:
            generos.append(cls(genero))
        return generos
    
    @classmethod
    def get_genero_y_libros(cls,data):
        query = "select * from generos left join libros on libros.genero_id=generos.id where generos.id=%(id)s;"
        resultados = connectToMySQL(cls.db_schema).query_db(query,data)
        genero = cls(resultados[0])
        for libro in resultados:
            datos = {
                "id" : libro['libros.id'],
                "nombre" : libro['libros.nombre'],
                "numero_paginas" : libro['numero_paginas'],
                "overview" : libro['overview'],
                "created_at" : libro['libros.created_at'],
                "updated_at" : libro['libros.updated_at']
            }
            genero.libros.append(Libro(datos))

        return genero
