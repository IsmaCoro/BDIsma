#archivo que almacena las credenciales de la base de datos
""""La exportacion de la BD al pypmyadmin solo funciona con el MAMP"""
import os

class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'practica'
    SECRET_KEY = 'mysecretkey'
