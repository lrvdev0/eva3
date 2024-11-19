from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para la página principal con los botones
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1 - Formulario de notas
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Obtener datos del formulario
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calcular promedio y estado
        promedio = (nota1 + nota2 + nota3) / 3
        estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'

        return render_template('ejercicio1_resultado.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')

# Ejercicio 2 - Formulario de nombres
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Calcular el nombre más largo
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

        return render_template('ejercicio2_resultado.html', nombre=nombre_mas_largo, longitud=longitud)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
