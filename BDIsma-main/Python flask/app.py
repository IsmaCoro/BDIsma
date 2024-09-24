from datetime import date
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'practica'
mysql = MySQL(app)

# Configuraciones
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM templeados')
    data = cur.fetchall()
    return render_template('Index.html', empleados=data)

@app.route('/Agregar_Empleado', methods=['POST'])
def Agregar_Empleado():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        rfc = request.form['RFC']
        nss = request.form['NSS']
        fecha_nacimiento = request.form['FechaNacimiento']
        fecha_ingreso = request.form['FechaIngreso']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO templeados (Nombre, RFC, NSS, FechaNacimiento, FechaIngreso) VALUES (%s, %s, %s, %s, %s)',
                    (nombre, rfc, nss, fecha_nacimiento, fecha_ingreso))
        mysql.connection.commit()
        flash('El empleado ha sido guardado exitosamente')
        return redirect(url_for('Index'))

@app.route('/VerEmpleadosRegistrados')
def Ver_Empleados_Registrados():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM templeados")
    empleados = cur.fetchall()
    return render_template('VerEmpleadosRegistrados.html', empleados=empleados)

@app.route('/Eliminar_Empleado/<string:id>')
def Eliminar_Empleado(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM templeados WHERE ID = %s', (id,))
    mysql.connection.commit()
    flash('El empleado ha sido eliminado correctamente')
    return redirect(url_for('Ver_Empleados_Registrados'))

@app.route('/Modificar_Empleado/<id>', methods=['GET', 'POST'])
def Modificar_Empleado(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        nombre = request.form['Nombre']
        rfc = request.form['RFC']
        nss = request.form['NSS']
        fecha_nacimiento = request.form['FechaNacimiento']
        fecha_ingreso = request.form['FechaIngreso']

        cur.execute('UPDATE templeados SET Nombre=%s, RFC=%s, NSS=%s, FechaNacimiento=%s, FechaIngreso=%s WHERE ID=%s',
                    (nombre, rfc, nss, fecha_nacimiento, fecha_ingreso, id))
        mysql.connection.commit()
        flash('El empleado ha sido modificado exitosamente')
        return redirect(url_for('Ver_Empleados_Registrados'))  

    cur.execute('SELECT * FROM templeados WHERE ID = %s', (id,))
    empleado = cur.fetchone()
    return render_template('EditarEmpleado.html', empleado=empleado)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
