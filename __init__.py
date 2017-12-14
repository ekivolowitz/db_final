from flask import Flask, render_template, request
from pprint import pprint
import sqlite3 as sql
import json
import sys
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/view')
def view():
    return render_template('view.html')
@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/bonus')
def bonus():
    return render_template('bonus.html')

@app.route('/queryStudentBonus')
def queryStudentBonus():
    pass

@app.route('/queryCourseBonus')
def queryCourseBonus():
    pass

@app.route('/queryDepartmentBonus', methods=['GET', 'POST'])
def queryDepartmentBonus():
    val = request.form['dept_name']
    try:
        con = sql.connect("data.db")
        con.row_factory = sql.Row
    
        cur = con.cursor()
        cur.execute("select * from Department d where d.Name = '" + val + "'")
        row = cur.fetchone()
        if row is None:
            raise IOError
        return render_template('bonus.html', department = row, queryType = 'Department')
    except:
        return render_template('bonus.html', department = None, queriedId = val, queryType = 'Department')
# TODO
def addDepartmentInsert(cur, deptId, deptName, address):
    sqlCommand = '''INSERT INTO Department (DID, Name, Address) VALUES(?, ?, ?)'''
    cur.execute(sqlCommand, (deptId, deptName, address))

# TODO
def addStudentInsert(cur, StudentID, Name, Year, Major):
    sqlCommand = "INSERT INTO Student (StudentID, Name, Year, Major) VALUES(?, ?, ?, ?)"
    cur.execute(sqlCommand, (StudentID, Name, Year, Major))

# TODO
def addTakesInsert(cur,):
    pass

# TODO
def addChairInsert(cur,):
    pass

# TODO
def addCanEnrollInsert(cur,):
    pass

# TODO
def addStaffInsert(cur,):
    pass

# TODO
def addCourseDescriptionInsert(cur,):
    pass

# TODO
def addCourseInstanceInsert(cur,):
    pass

# TODO
def addProfessorInsert(cur,):
    pass

# TODO
def addAdminInsert(cur,):
    pass

# TODO
def addBuildingInsert(cur,):
    pass

# TODO
def addRoomInsert(cur,):
    pass


# TODO
def errorCheckHelperDepartment(DID, Name, Address):
    errorString = ""
    if len(DID) > 30:
        errorString += "Length of DID must be less than 30 characters.\n"
    if len(Name) > 50:
        errorString += "Length of Name must be less than 50\n"
    if len(Address) > 255:
        errorString += "Length of Address must be less than 255 characters\n"
    return errorString

# TODO
def errorCheckHelperStudent():
    pass

# TODO
def errorCheckHelperTakes():
    pass

# TODO
def errorCheckHelperChair():
    pass

# TODO
def errorCheckHelperCanEnroll():
    pass

# TODO
def errorCheckHelperStaff():
    pass

# TODO
def errorCheckHelperCourseDescription():
    pass

# TODO
def errorCheckHelperCourseInstance():
    pass

# TODO
def errorCheckHelperProfessor():
    pass

# TODO
def errorCheckHelperAdmin():
    pass

# TODO
def errorCheckHelperBuilding():
    pass

# TODO
def errorCheckHelperRoom():
    pass

def valueIsNotInDB(cur, sqlStatement):
    cur.execute(sqlStatement)
    row = cur.fetchone()
    if row is not None:
        return True
    return False


@app.route('/addDepartment', methods = ['POST', 'GET'])
def addDepartment():
    with sql.connect('data.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()if request.form['file'] == "":
        sqlStatement = "select * from {} where {}"
        jsonInput = request.form['input']
        jsonValue = json.loads(jsonInput)
        
        if len(jsonValue) > 1:
            # ERROR
            pass
        for element in jsonValue:
            if element == "Department":
                try:
                    DID = element['DID']
                    Name = element['Name']
                    Address = element['Address']
                except:
                    #ERROR  did not have a field did, name, or address
                    pass
                search = sqlStatement.format(element, "DID = " + DID)
                if valueIsNotInDB(cur, search):
                    # insert
                    addDepartmentInsert(cur, DID, Name, Address)
                else:
                    # ERROR value was already in the database.
                
            elif element == "Student":
                try:
                    StudentID = element['StudentID']
                    Name = element['Name']
                    Year = element['Year']
                    Major = element['Major']
                except:
                    # ERROR
                    pass
            elif element == "Takes":
                try:
                    StudentID = element['StudentID']
                    CID = element['CID']
                    Semester = element['Semester']
                    Year = element['Year']
                except:
                    # ERROR
                    pass
            elif element == "Chair":
                try:
                    DID = element['DID']
                    SID = element['SID']
                except:
                    # ERROR 
                    pass 
            elif element == "CanEnroll":
                try:
                    SID = element['SID']
                    CID = element['CID']
                except:
                    # ERROR
                    pass
            elif element == "Staff":
                try:
                    SID = element['SID']
                    DID = element['DID']
                    Name = element['Name']
                    Age = int(element['Age'])
                except:
                    # ERROR 
                    pass
            elif element == "CourseDescription":
                try:
                    CID = element['CID']
                    Name = element['Name']
                    Credits = element['Credits']
                except:
                    # ERROR 
                    pass
            elif element == "CourseInstance":
                try:
                    CID = element['CID']
                    Semester = element['Semester']
                    Year = element['Year']
                    SID = element['SID']
                    IsOpen = element['IsOpen']
                    BID = element['BID']
                    RoomNumber = element['RoomNumber']
                except:
                    # ERROR 
                    pass
            elif element == "Professor":
                try:
                    SID = element['SID']
                    Tenure = element['Tenure']
                    RoomNumber = element['RoomNumber']
                except:
                    # ERROR
                    pass
            elif element == "Admin":
                try:
                    SID = element['SID']
                    RoomNumber = element['RoomNumber']
                except:
                    # ERROR 
                    pass
            elif element == "Building":
                try:
                    BID = element['BID']
                    DID = element['DID']
                    Name = element['Name']
                    NumRooms = element['NumRooms']
                except:
                    pass
            elif element == "Room":
                try:
                    BID = element['BID']
                    RoomNumber = element['RoomNumber']
                    Capacity = element['Capacity']
                except:
                    # ERROR
                    pass
            else:
                pass

        # if len(deptId) > 30 or len(deptName) > 50 or len(address) > 255:
        #     print("In the error string")
        #     errorString = ""
        #     if len(deptId) > 30:
        #         errorString += "Department ID cannot be more than 30 characters.\n"
        #     if len(deptName) > 50:
        #         errorString += "Department Name cannot be more than 50 characters.\n"
        #     if len(address) > 255:
        #         errorString += "Department Address cannot be more than 255 characters.\n"
        #     return render_template('insert.html', error = "ERROR: " + errorString, ran = 1)
        
        
        # try:
        #     with sql.connect('data.db') as con:
        #         con.row_factory = sql.Row
        #         cur = con.cursor()
                
        #         cur.execute("select * from Department where DID = '" + deptId + "'")
        #         row = cur.fetchone()
        #         if row is not None:
        #             print("DepartmentID exists already")
        #             return render_template("insert.html", error = "ERROR: A department with Department ID " + deptId + " exists already.", ran = 1)
        #         addDepartmentInsert(deptId, deptName, address, cur)
        #         return render_template('insert.html', error = None)

        # except:
        #     return render_template('insert.html', error = "ERROR: INSERTION ERROR", ran = 1)
    else:
        try:
            
            j = open(request.form['file'], 'r')
            
            jsonFile = json.load(j)
            pprint(jsonFile)
            errorString = ""
            with sql.connect('data.db') as con:
                con.row_factory = sql.Row
                cur = con.cursor()
                for dept in jsonFile:
                    print(dept)
                    cur.execute("select * from Department where DID = '" + dept + "'")
                    print("Finished query to check if it exists")
                    row = cur.fetchone()
                    if row is not None:
                        # print("DepartmentID exists already")
                        errorString += "A department with Department ID " + dept + " already exists.\n"
                    else:
                        addDepartmentInsert(dept, jsonFile[dept]['Name'], jsonFile[dept]['Address'], cur)
                
                
                if errorString == "":
                    return render_template('insert.html', error = None, ran = 1)
                else:
                    return render_template('insert.html', error = "ERROR: " + errorString, ran = 1)
        except:
            print("Error in the bulk upload.")
    return render_template("insert.html")



# View Tables query based on name
@app.route('/viewQuery', methods = ['POST', 'GET'])
def viewQuery():
    print("Running here")
    val = request.form['table']
    page = request.form['pageNo']
    perPage = request.form['perPage']
    page = str(int(page) - 1)
    
    offset = int(perPage) * int(page)

    try:
        con = sql.connect("data.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from " + val + " limit '" + str(perPage) + "' offset '" + str(offset) + "'")
        rows = cur.fetchall()
        if rows is None:
            raise IOError
        return render_template('view.html', view = rows, queryType = val)
    except:
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
