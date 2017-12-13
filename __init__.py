from flask import Flask, render_template, request
from pprint import pprint
import sqlite3 as sql
import sys
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/view')
def view():
    return render_template('view.html')


# View Tables query based on name
@app.route('/viewQuery', methods = ['POST', 'GET'])
def viewQuery():
    print("Running here")
    val = request.form['table']
    page = request.form['pageNo']
    perPage = request.form['perPage']
    page = str(int(page) - 1)
    
    offset = int(perPage) * int(page)
    print("Val is: " + str(val))
    print("page is: " + str(page))
    print("perPage is: " + str(perPage))
    print("Offset is: " + str(offset))
    try:
        print("Running try statement")
        con = sql.connect("data.db")
        print("Connected to sql")
        con.row_factory = sql.Row
        print("Not sure what the row factory does")
        cur = con.cursor()
        print("Connected to cursor")
        # cur.execute("select * from '" + table + "' limit '" + perPage + "' offset '" + offset "'")
        # cur.execute("select * from " + val + " limit " + perPage + " offset " + offset)
        cur.execute("select * from " + val + " limit '" + str(perPage) + "' offset '" + str(offset) + "'")
        rows = cur.fetchall()
        if rows is None:
            raise IOError
        print("Printing rows")
        for row in rows:
            print("Row is " + str(row))
        return render_template('view.html', view = rows, queryType = val)
    except:
        print("Rows was none")
        return render_template('view.html', view = None, queriedId = val, queryType = val)
   
@app.route('/query')
def queryStudentHomePage():
    return render_template('search.html')

@app.route('/Student', methods = ['POST', 'GET'])
def queryStudent():
    val = request.form['id']
    try:
        con = sql.connect("data.db")
        con.row_factory = sql.Row
    
        cur = con.cursor()
        cur.execute("select * from Student s where s.StudentId = " + val)
        row = cur.fetchone()
        if row is None:
            raise IOError
        return render_template('search.html', student=row, queryType = "Student")
    except:
        return render_template('search.html', student = None, queriedId = val, queryType = "Student")

@app.route('/course', methods = ['POST', 'GET'])
def queryCourse():
    val = request.form['cid']
    try:
        con = sql.connect("data.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from CourseDescription c where c.CID = '" + str(val) + "'")
        
        row = cur.fetchone()
        if row is None:
            raise IOError
        return render_template('search.html', course = row, queryType = 'Course')
    except:
        return render_template('search.html', course = None, queriedId = val, queryType = 'Course')





@app.route('/Department', methods = ['POST', 'GET'])
def queryDepartment():
    val = request.form['dept_id']
    try:
        con = sql.connect("data.db")
        con.row_factory = sql.Row
    
        cur = con.cursor()
        cur.execute("select s.Name, d.Name FROM Staff s, Chair c, Department d where s.SID = c.SID AND '" + val + "' = c.DID")
        row = cur.fetchone()
        if row is None:
            raise IOError
        return render_template('search.html', department = row, queryType = 'Department')
    except:
        return render_template('search.html', department = None, queriedId = val, queryType = 'Department')


if __name__ == '__main__':
   app.run(debug = True)
