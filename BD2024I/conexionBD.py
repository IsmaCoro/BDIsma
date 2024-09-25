#archivo que se encarga de realizar la conexion a la base de datos
from flask_mysqldb import MySQL
from flask import Flask
from config import Config

def init_db(app: Flask):
    app.config.from_object(Config)
    mysql = MySQL(app)
    return mysql
