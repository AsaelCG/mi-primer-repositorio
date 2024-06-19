from flask import Flask, render_template
from entidades.estudiante import Estudiante
from entidades.profesor import Profesor
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

@app.route("/profesores")
def profesores():
    profesores=[]
    with open ('db/profesores.txt', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            id, nombre, ap_paterno, ap_materno = line.split('|')
            profresor1= Profesor(id, nombre, ap_paterno, ap_materno)
            profesores.append(profresor1)
    return render_template('profesores.html', data=profesores)

@app.route("/materias")
def materias ():
    materias = []
    with open ('db/materias.txt', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            cortadoras = line.split('|')
            materias.append({'nombre' : cortadoras[0], 'calificacion' : cortadoras[1]})
    return render_template ('materias.html', data = materias)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)