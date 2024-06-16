from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html',stylefile="static/style.css")
@app.route('/m1')
def m1():
    with sql.connect("data/museum.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM muzeler WHERE  id = 1")
        data = cur.fetchall()
        title = data[0][1]
        info = data[0][2]
        googleMap = data[0][3]
        muzelink=data[0][4]
        pic = data[0][5]
    return render_template('museum.html',stylefile="static/style.css",title=title,info=info,muzelink=muzelink,googleMap=googleMap,pic=pic)
@app.route('/m2')
def m2():
    with sql.connect("data/museum.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM muzeler WHERE  id = 2")
        data = cur.fetchall()
        title = data[0][1]
        info = data[0][2]
        googleMap = data[0][3]
        muzelink=data[0][4]
        pic = data[0][5]
    return render_template('museum.html',stylefile="static/style.css",title=title,info=info,muzelink=muzelink,googleMap=googleMap,pic=pic)
@app.route('/m3')
def m3():
    with sql.connect("data/museum.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM muzeler WHERE  id = 3")
        data = cur.fetchall()
        title = data[0][1]
        info = data[0][2]
        googleMap = data[0][3]
        muzelink=data[0][4]
        pic = data[0][5]
    return render_template('museum.html',stylefile="static/style.css",title=title,info=info,muzelink=muzelink,googleMap=googleMap,pic=pic)
@app.route('/m4')
def m4():
    with sql.connect("data/museum.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM muzeler WHERE  id = 4")
        data = cur.fetchall()
        title = data[0][1]
        info = data[0][2]
        googleMap = data[0][3]
        muzelink=data[0][4]
        pic = data[0][5]
    return render_template('museum.html',stylefile="static/style.css",title=title,info=info,muzelink=muzelink,googleMap=googleMap,pic=pic)
@app.route('/m5')
def m5():
    with sql.connect("data/museum.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM muzeler WHERE  id = 5")
        data = cur.fetchall()
        title = data[0][1]
        info = data[0][2]
        googleMap = data[0][3]
        muzelink=data[0][4]
        pic = data[0][5]
    return render_template('museum.html',stylefile="static/style.css",title=title,info=info,muzelink=muzelink,googleMap=googleMap,pic=pic)
@app.route('/m6')
def m6():
    with sql.connect("data/museum.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM muzeler WHERE  id = 6")
        data = cur.fetchall()
        title = data[0][1]
        info = data[0][2]
        googleMap = data[0][3]
        muzelink=data[0][4]
        pic = data[0][5]
    return render_template('museum.html',stylefile="static/style.css",title=title,info=info,muzelink=muzelink,googleMap=googleMap,pic=pic)
@app.route('/m7')
def m7():
    with sql.connect("data/museum.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM muzeler WHERE  id = 7")
        data = cur.fetchall()
        title = data[0][1]
        info = data[0][2]
        googleMap = data[0][3]
        muzelink=data[0][4]
        pic = data[0][5]
    return render_template('museum.html',stylefile="static/style.css",title=title,info=info,muzelink=muzelink,googleMap=googleMap,pic=pic)
@app.route('/m8')
def m8():
    with sql.connect("data/museum.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM muzeler WHERE  id = 8")
        data = cur.fetchall()
        title = data[0][1]
        info = data[0][2]
        googleMap = data[0][3]
        muzelink=data[0][4]
        pic = data[0][5]
    return render_template('museum.html',stylefile="static/style.css",title=title,info=info,muzelink=muzelink,googleMap=googleMap,pic=pic)
@app.route('/m9')
def m9():
    with sql.connect("data/museum.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM muzeler WHERE  id = 9")
        data = cur.fetchall()
        title = data[0][1]
        info = data[0][2]
        googleMap = data[0][3]
        muzelink=data[0][4]
        pic = data[0][5]
    return render_template('museum.html',stylefile="static/style.css",title=title,info=info,muzelink=muzelink,googleMap=googleMap,pic=pic)
@app.route('/m10')
def m10():
    with sql.connect("data/museum.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM muzeler WHERE  id = 10")
        data = cur.fetchall()
        title = data[0][1]
        info = data[0][2]
        googleMap = data[0][3]
        muzelink=data[0][4]
        pic = data[0][5]
    return render_template('museum.html',stylefile="static/style.css",title=title,info=info,muzelink=muzelink,googleMap=googleMap,pic=pic)