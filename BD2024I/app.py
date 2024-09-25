#importamos las funciones para el uso del flask
from flask import Flask, flash, redirect, render_template, request, url_for
#agregamos el archivo que tiene la conexion a la base de datos
from conexionBD import init_db
#importamos las funciones del archivo models
from models import get_empleados, agregar_empleado, eliminar_empleado, modificar_empleado

app = Flask(__name__)
mysql = init_db(app)

#Mostramos la pagina de login
@app.route('/')
def login():
    return render_template('Login.html')

#para mostrar la pagina despues del login
@app.route('/login', methods=['POST'])
def user():
    usuario = request.form['username']
    return render_template("Index.html", modo=usuario)

#para cuando se de click en el boton Entrada
@app.route('/Index')
def index():
    empleados = get_empleados(mysql)
    return render_template('Index.html', empleados=empleados)


#funcion para el boton que registra a los empleados
@app.route('/Agregar_Empleado', methods=['POST'])
def agregar_empleado_route():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        rfc = request.form['RFC']
        nss = request.form['NSS']
        fecha_nacimiento = request.form['FechaNacimiento']
        fecha_ingreso = request.form['FechaIngreso']
        sucursal_id = 1
        colonia_id = 1
        contactoemergencia_id = 1

        #ejecutamos la funcion externa que se encarga de subir los datos a la BD
        agregar_empleado(mysql, nombre, rfc, nss, fecha_nacimiento, fecha_ingreso, sucursal_id, colonia_id, contactoemergencia_id)
        flash('El empleado ha sido guardado exitosamente')
        return redirect(url_for('index'))

#funcion para el boton que muestra el html con los empleados registrados
@app.route('/VerEmpleadosRegistrados', methods=['POST'])
def Ver_Empleados_Registrados():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM templeados")
    empleados = cur.fetchall()
    usuario = request.form['modo']
    if usuario == "Admin":
        modo = usuario
        return render_template("VerEmpleadosRegistrados.html", empleados=empleados, modo=modo)

    else:
        modo = usuario
        return render_template('VerEmpleadosRegistrados.html', empleados=empleados, modo=modo)

#funcion para el boton que esta en la pagina de EditarEmpleado y elimina al empleado
@app.route('/Eliminar_Empleado/<string:id>')
def eliminar_empleado_route(id):
    eliminar_empleado(mysql, id)
    flash('El empleado ha sido eliminado correctamente')
    return redirect(url_for('index'))

#funcion para el boton de EditarEmpleado para modificar al empleado seleccionado
@app.route('/Modificar_Empleado/<id>', methods=['GET', 'POST'])
def modificar_empleado_route(id):
    if request.method == 'POST':
        nombre = request.form['Nombre']
        rfc = request.form['RFC']
        nss = request.form['NSS']
        fecha_nacimiento = request.form['FechaNacimiento']
        fecha_ingreso = request.form['FechaIngreso']
        modificar_empleado(mysql, id, nombre, rfc, nss, fecha_nacimiento, fecha_ingreso)
        flash('El empleado ha sido modificado exitosamente')
        return redirect(url_for('index'))

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM templeados WHERE ID = %s', (id,))
    empleado = cur.fetchone()
    return render_template('EditarEmpleado.html', empleado=empleado)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
