from flask import Flask, render_template, request
from pprint import pprint
import sqlite3 as sql
import sys
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

# Test code from Adel's set up instructions.
# @app.route('/addrec',methods = ['POST', 'GET'])
# def addrec():
#    if request.method == 'POST':
#       try:
#          nm = request.form['nm']
#          addr = request.form['add']
#          city = request.form['city']
#          pin = request.form['pin']
         
#          with sql.connect("database.db") as con:
#             cur = con.cursor()
            
#             cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)"
#                 ,(nm,addr,city,pin) )
            
#             con.commit()
#             msg = "Record successfully added"
#       except:
#          con.rollback()
#          msg = "error in insert operation"
      
#       finally:
#          return render_template("result.html",msg = msg)
#          con.close()

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
        cur.execute("select * from Department d where d.DID = '" + val + "'")
        row = cur.fetchone()
        if row is None:
            raise IOError
        return render_template('search.html', department = row, queryType = 'Department')
    except:
        return render_template('search.html', department = None, queriedId = val, queryType = 'Department')


if __name__ == '__main__':
   app.run(debug = True)
