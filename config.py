from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)
app.secret_key = "hybrid_security"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your password'   
app.config['MYSQL_DB'] = 'hybrid_security'
mysql = MySQL(app)