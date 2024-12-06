from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.genero import Genero
from flask_app.models.libro import Libro



@app.route('/')

def main():
    generos = Genero.get_all()
    libros = Libro.get_all()
    print(generos)
    print(libros)
    return render_template('index.html',generos = generos, libros = libros)


@app.route('/generos/filtro', methods=['POST'])
def cursos_filtro():
    data = {
        'id': request.form['genero_id']
    }
    genero = Genero.get_genero_y_libros(data)
    generos = Genero.get_all()
    return render_template('genero_libros.html',generos=generos, genero=genero)