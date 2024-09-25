#archivo que contiene los comandos para las consultas en la base de datos
from flask_mysqldb import MySQL

#obtenemos todos los datos de lo empleados
def get_empleados(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM templeados')
    return cur.fetchall()

#agregamos datos a un empleado (Registro)
def agregar_empleado(mysql, nombre, rfc, nss, fecha_nacimiento, fecha_ingreso, sucursal_id, colonia_id, contactoemergencia_id):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO templeados (Nombre, RFC, NSS, FechaNacimiento, FechaIngreso, TSucursal_ID, TColonias_ID, TContactoEmergencia_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (nombre, rfc, nss, fecha_nacimiento, fecha_ingreso, sucursal_id, colonia_id, contactoemergencia_id))
    mysql.connection.commit()

#eliminamos los datos de un usuario por id
def eliminar_empleado(mysql, id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM templeados WHERE ID = %s', (id,))
    mysql.connection.commit()

#modificamos los datos de un usuario
def modificar_empleado(mysql, id, nombre, rfc, nss, fecha_nacimiento, fecha_ingreso):
    cur = mysql.connection.cursor()
    cur.execute('UPDATE templeados SET Nombre=%s, RFC=%s, NSS=%s, FechaNacimiento=%s, FechaIngreso=%s WHERE ID=%s',
                (nombre, rfc, nss, fecha_nacimiento, fecha_ingreso, id))
    mysql.connection.commit()
