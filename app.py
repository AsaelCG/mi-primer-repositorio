from flask import Flask, render_template

app = Flask(__name__)

@app.route ("/")
def index():
    return render_template('index.html')

@app.route ("/estudiantes")
def estudiantes():
    data = [
        {"matricula" : "230702", "nombre": "Asael", "apellido_paterno": "Cisneros", "apellido_materno" : "Gonzalez"},
        {"matricula" : "230678", "nombre": "Jamila", "apellido_paterno": "Cisneros", "apellido_materno" : "Gonzalez"},
        {"matricula" : "230973", "nombre": "Vanessa", "apellido_paterno": "Villalobos", "apellido_materno" : "Villalobos"}
    ]
    return render_template('estudiantes.html', data=data)

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