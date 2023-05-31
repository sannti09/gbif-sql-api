from flask import Flask, render_template
import cx_Oracle, json

username = 'is327200'
password = 'Ve0ZRVqAmR'
host = 'orion.javeriana.edu.co'
port = '1521'
service_name = 'INGSIS'
database_name = 'LAB'

dsn = cx_Oracle.makedsn(host, port, service_name, database_name)
connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
cursor = connection.cursor()


app = Flask(__name__)

opciones = ["punto1", "punto2", "punto3", "punto4", "punto5", "punto6", "punto7", "punto8", "punto9"]


@app.route('/')
def index():
    return render_template('index.html', pag='punto1', opciones=opciones)

@app.route('/deployment')
def deployment():
    cursor.execute("SELECT * FROM Deployment")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    print(rows)

    return render_template('base.html', rows=rows, headers=headers)

@app.route('/media')
def media():
    cursor.execute("SELECT * FROM Media")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('base.html', rows=rows, headers=headers)

@app.route('/observation')
def observation():
    cursor.execute("SELECT * FROM Observation")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('base.html', rows=rows, headers=headers)



@app.route('/punto1')
def punto1():
    cursor.execute("SELECT * FROM punto1")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows, headers=headers, pag='punto1', opciones=opciones)

@app.route('/punto2')
def punto2():
    cursor.execute("SELECT * FROM punto2")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows, headers=headers, pag='punto2', opciones=opciones)

@app.route('/punto3')
def punto3():
    cursor.execute("SELECT * FROM punto3")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows, headers=headers, pag='punto3', opciones=opciones)

@app.route('/punto4')
def punto4():
    cursor.execute("SELECT * FROM punto4")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows, headers=headers, pag='punto4', opciones=opciones)

@app.route('/punto5')
def punto5():
    cursor.execute("SELECT * FROM punto5")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows, headers=headers, pag='punto5', opciones=opciones)

@app.route('/punto6')
def punto6():
    cursor.execute("SELECT * FROM punto6")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows, headers=headers, pag='punto6', opciones=opciones)

@app.route('/punto7')
def punto7():
    cursor.execute("SELECT * FROM punto7")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows, headers=headers, pag='punto7', opciones=opciones)

@app.route('/punto8')
def punto8():
    cursor.execute("SELECT * FROM punto8")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows, headers=headers, pag='punto8', opciones=opciones)

@app.route('/punto9')
def punto9():
    cursor.execute("SELECT * FROM punto9")
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows, headers=headers, pag='punto9', opciones=opciones)

if __name__ == '__main__':
    app.run()