from flask import Flask, render_template
from entidades.estudiante import Estudiante
app = Flask(__name__)

@app.route ("/")
def index():
    return render_template('index.html')

@app.route ("/estudiantes")
def estudiantes():
    estudiantes = []
    with open ('db/estudiantes.txt', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            matricula, nombre, ap_paterno, ap_materno = line.split('|')
            estudiante1 = Estudiante(matricula, nombre, ap_paterno, ap_materno)
            estudiantes.append(estudiante1)
    return render_template('estudiantes.html', data=estudiantes)

@app.route("/materias")
def materias ():
    materias = [
        {"nombre":"Analisis y Diseños de Algoritmos", "calificacion": 10},
        {"nombre":"Programación Orientada a Objetos", "calificacion": 9},
        {"nombre":"Bases de datos", "calificacion": 7},
        {"nombre":"Programación Avanzada", "calificacion": 10}
    ]
    return render_template ('materias.html', materias = materias)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)