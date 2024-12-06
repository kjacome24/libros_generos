from flask_app.config.mysqlconnection import connectToMySQL ###Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos
#####aqui debes importar otras clases en caso de que sea necesario


class Libro:
    db_schema = 'libros_genero' ## Cambiar la BD a la que estamos apuntando
    def __init__(self,data):
# Agregar el los  atributos que vienen de la Base de datos
        self.id = data['id'] 
        self.nombre = data['nombre']
        self.numero_paginas = data['numero_paginas']
        self.overview = data['overview']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "select * from libros;" ###cambiar la tabla a la que apuntamos.
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        libros = [] ###Cambiar el nombre del arreglo para algo que represente la tabla
        for libro in resultados:
            libros.append(cls(libro))
        return libros
