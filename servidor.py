from flask import Flask, render_template
from bd import *
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)



app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade'


@app.route('/')
def inicio():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)