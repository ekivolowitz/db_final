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

@app.route('/queryStudentBonus', methods=['POST', 'GET'])
def queryStudentBonus():
    val = request.form['studentname']
    with sql.connect("data.db") as con:
        try:
            con.row_factory = sql.Row
        
            cur = con.cursor()
            cur.execute("select * from Student s where s.Name like '" + val + "%' limit 150")
            rows = cur.fetchall()
            if rows is None:
                raise IOError
            print("Before printing stuff")
            for row in rows:
                print("Row")
                for val in row:
                    print("Val in row:" + val)
            return render_template('bonus.html', student=rows, queryType = "Student", run = 1)
        except:
            return render_template('bonus.html', student = None, queriedId = val, queryType = "Student", run = 1)

@app.route('/queryCourseBonus', methods=['POST', 'GET'])
def queryCourseBonus():
    pass

@app.route('/queryDepartmentBonus', methods=['GET', 'POST'])
def queryDepartmentBonus():
    val = request.form['dept_name']
    try:
        con = sql.connect("data.db")
        con.row_factory = sql.Row
    
        cur = con.cursor()
        cur.execute("select * from Department d where d.Name like '" + val + "%' limit 150")
        row = cur.fetchall()
        if row is None:
            raise IOError
        return render_template('bonus.html', department = row, queryType = 'Department')
    except:
        return render_template('bonus.html', department = None, queriedId = val, queryType = 'Department')



def addDepartmentInsert(cur, deptId, deptName, address):
    sqlCommand = "INSERT INTO Department (DID, Name, Address) VALUES(?, ?, ?)"
    cur.execute(sqlCommand, (deptId, deptName, address))

def addStudentInsert(cur, StudentID, Name, Year, Major):
    sqlCommand = "INSERT INTO Student (StudentID, Name, Year, Major) VALUES(?, ?, ?, ?)"
    cur.execute(sqlCommand, (StudentID, Name, Year, Major))

def addTakesInsert(cur, StudentID, CID, Semester, Year):
    sqlCommand = "INSERT INTO Takes (StudentID, CID, Semester, Year) VALUES(?, ?, ?, ?)"
    cur.execute(sqlCommand, (StudentID, CID, Semester, Year))

def addChairInsert(cur, DID, SID):
    sqlCommand = "INSERT INTO Chair (DID, SID) VALUES(?, ?)"
    cur.execute(sqlCommand, (DID, SID))

def addCanEnrollInsert(cur, SID, CID):
    sqlCommand = "INSERT INTO CanEnroll (SID, CID) VALUES(?, ?)"
    cur.execute(sqlCommand, (SID, CID))

def addStaffInsert(cur, SID, DID, Name, Age):
    sqlCommand = "INSERT INTO Staff (SID, DID, Name, Age) VALUES(?, ?, ?, ?)"
    cur.execute(sqlCommand, (SID, DID, Name, Age))

def addCourseDescriptionInsert(cur, CID, Name, Credits):
    sqlCommand = "INSERT INTO CourseDescription (CID, Name, Credits) VALUES(?, ?, ?)"
    cur.execute(sqlCommand, (CID, Name, Credits))

def addCourseInstanceInsert(cur, CID, Semester, Year, SID, IsOpen, BID, RoomNumber):
    sqlCommand = "INSERT INTO CourseInstance (CID, Semester, Year, SID, IsOpen, BID, RoomNumber) VALUES(?, ?, ?, ?, ?, ?, ?)"
    cur.execute(sqlCommand, (CID, Semester, Year, SID, IsOpen, BID, RoomNumber))

def addProfessorInsert(cur, SID, Tenure, RoomNumber):
    sqlCommand = "INSERT INTO Professor (SID, Tenure, RoomNumber) VALUES(?, ?, ?)"
    cur.execute(sqlCommand, (SID, Tenure, RoomNumber))

def addAdminInsert(cur, SID, RoomNumber):
    sqlCommand = "INSERT INTO Admin (SID, RoomNumber) VALUES(?, ?)"
    cur.execute(sqlCommand, (SID, RoomNumber))

def addBuildingInsert(cur, BID, DID, Name, NumRooms):
    sqlCommand = "INSERT INTO Building (BID, DID, Name, NumRooms) VALUES(?, ?, ?, ?)"
    cur.execute(sqlCommand, (BID, DID, Name, NumRooms))

def addRoomInsert(cur, BID, RoomNumber, Capacity):
    sqlCommand = "INSERT INTO Room (BID, RoomNumber, Capacity) VALUES(?, ?, ?)"
    cur.execute(sqlCommand, (BID, RoomNumber, Capacity))

def errorCheckHelperDepartment(DID, Name, Address):
    errorString = ""
    if len(DID) > 30:
        errorString += "Length of DID must be less than or equal to 30 characters.\n"
    if len(Name) > 50:
        errorString += "Length of Name must be less than or equal to 50 characters.\n"
    if len(Address) > 255:
        errorString += "Length of Address must be less than or equal to 255 characters\n"
    return errorString
def errorCheckHelperStudent(StudentID, Name, Year, Major):
    errorString = ""
    if len(StudentID) > 50:
        errorString += "Length of StudentID must be less than or equal to 50 characters.\n"
    if len(Name) > 30:
        errorString += "Length of Name must be less than or equal to 30 characters.\n"
    if len(Year) > 5:
        errorString += "Length of Year must be less than or equal to 5 characters\n"
    if len(Major) > 30:
        errorString += "Length of Major must be less than or equal to 30 characters.\n"
    return errorString
def errorCheckHelperTakes(StudentID, CID, Semester, Year):
    errorString = ""
    if len(StudentID) > 50:
        errorString += "Length of StudentID must be less than or equal to 50 characters.\n"
    if len(CID) > 50:
        errorString += "Length of CID must be less than or equal to 50 characters.\n"
    if len(Year) > 5:
        errorString += "Length of Year must be less than or equal to 5 characters\n"
    if len(Semester) > 30:
        errorString += "Length of Semester must be less than or equal to 30 characters.\n"
    return errorString
def errorCheckHelperChair(DID, SID):
    errorString = ""
    if len(DID) > 50:
        errorString += "Length of DID must be less than or equal to 50 characters.\n"
    if len(SID) > 50:
        errorString += "Length of SID must be less than or equal to 50 characters.\n"
    return errorString
def errorCheckHelperCanEnroll(SID, CID):
    errorString = ""
    if len(CID) > 50:
        errorString += "Length of CID must be less than or equal to 50 characters.\n"
    if len(SID) > 50:
        errorString += "Length of SID must be less than or equal to 50 characters.\n"
    return errorString
def errorCheckHelperStaff(SID, DID, Name, Age):
    errorString = ""
    if len(SID) > 50:
        errorString += "Length of SID must be less than or equal to 50 characters.\n"
    if len(DID) > 50:
        errorString += "Length of DID must be less than or equal to 50 characters.\n"
    if len(Name) > 30:
        errorString += "Length of Name must be less than or equal to 30 characters\n"
    if int(Age) < 0:
        errorString += "Age must be greater than  or equal to 0.\n"
    return errorString
def errorCheckHelperCourseDescription(CID, Name, Credits):
    errorString = ""
    if len(CID) > 50:
        errorString += "Length of CID must be less than or equal to 50 characters.\n"
    if len(Name) > 30:
        errorString += "Length of Name must be less than or equal to 30 characters\n"
    if int(Credits) < 1:
        errorString += "Credits must be greater than 0.\n"
    return errorString
def errorCheckHelperCourseInstance(CID, Semester, Year, SID, IsOpen, BID, RoomNumber):
    errorString = ""
    if len(CID) > 50:
        errorString += "Length of CID must be less than or equal to 50 characters.\n"
    if len(Semester) > 30:
        errorString += "Length of Semester must be less than or equal to 30 characters.\n"
    if len(Year) > 5:
        errorString += "Length of Year must be less than or equal to 5 characters\n"
    if len(SID) > 50:
        errorString += "Length of SID must be less than or equal to 50 characters.\n"
    if int(IsOpen) < 0 or int(IsOpen) > 1:
        errorString += "IsOpen must be 0 or 1.\n"
    if len(BID) > 50:
        errorString += "Length of BID must be less than or equal to 50 characters.\n"
    if len(RoomNumber) > 10:
        errorString += "Length of RoomNumber must be less than or equal to 10 characters.\n"
    return errorString
def errorCheckHelperProfessor(SID, Tenure, RoomNumber):
    errorString = ""
    if len(SID) > 50:
        errorString += "Length of SID must be less than or equal to 50 characters.\n"
    if int(Tenure) < 0 or int(Tenure) > 1:
        errorString += "Tenure must be a boolean value.\n"
    if len(RoomNumber) > 10:
        errorString += "Length of RoomNumber must be less than or equal to 10 characters.\n"
    return errorString
def errorCheckHelperAdmin(SID, RoomNumber):
    errorString = ""
    if len(SID) > 50:
        errorString += "Length of SID must be less than or equal to 50 characters.\n"
    if len(RoomNumber) > 10:
        errorString += "Length of RoomNumber must be less than or equal to 10 characters.\n"
    return errorString
def errorCheckHelperBuilding(BID, DID, Name, NumRooms):
    errorString = ""
    if len(BID) > 50:
        errorString += "Length of BID must be less than or equal to 50 characters.\n"
    if len(DID) > 50:
        errorString += "Length of DID must be less than or equal to 50 characters.\n"
    if len(Name) > 30:
        errorString += "Length of Name must be less than or equal to 30 characters\n"
    if int(NumRooms) < 0:
        errorString += "NumRooms must be greater than or equal to 0.\n"
    return errorString
def errorCheckHelperRoom(BID, RoomNumber, Capacity):
    errorString = ""
    if len(BID) > 50:
        errorString += "Length of BID must be less than or equal to 50 characters.\n"
    if len(RoomNumber) > 10:
        errorString += "Length of RoomNumber must be less than or equal to 10 characters\n"
    if int(Capacity) < 0:
        errorString += "Capacity must be greater than or equal to 0.\n"
    return errorString

def valueIsInDB(cur, sqlStatement):
    cur.execute(sqlStatement)
    row = cur.fetchone()
    if row is not None:
        return True
    return False


@app.route('/addDepartment', methods = ['POST', 'GET'])
def addDepartment():
    with sql.connect('data.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        if request.form['file'] == "":
            sqlStatement = "select * from {} where {}"
            try:
                jsonInput = request.form['input']
                jsonValue = json.loads(jsonInput)
            except:
                return render_template("insert.html", error = "Malformatted JSON")
            print("Got here")
            if len(jsonValue) > 1:
                # ERROR
                pass
            print("JSON Value is 1")
            for element in jsonValue:
                print(element)
                if element == "Department":
                    try:
                        DID = jsonValue[element][0]['DID']
                        Name = jsonValue[element][0]['Name']
                        Address = jsonValue[element][0]['Address']
                        search = sqlStatement.format(element, "DID = '" + DID + "'")
                        if not valueIsInDB(cur, search):
                            # insert
                            addDepartmentInsert(cur, DID, Name, Address)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = DID + " already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have three fields: DID, Name, Address")
                    
                    
                elif element == "Student":
                    try:
                        StudentID = jsonValue[element][0]['StudentID']
                        Name = jsonValue[element][0]['Name']
                        Year = jsonValue[element][0]['Year']
                        Major = jsonValue[element][0]['Major']
                        search = sqlStatement.format(element, "StudentID = '" + StudentID + "'")
                        print(search)
                        if not valueIsInDB(cur, search):
                            # insert
                            addStudentInsert(cur, StudentID, Name, Year, Major)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = StudentID + " already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have four fields: StudentID, Name, Year, Major")
                        
                elif element == "Takes":
                    try:
                        StudentID = jsonValue[element][0]['StudentID']
                        CID = jsonValue[element][0]['CID']
                        Semester = jsonValue[element][0]['Semester']
                        Year = jsonValue[element][0]['Year']
                        
                        search = sqlStatement.format(element, "StudentID = '" + StudentID + "' AND " + "CID = '" + CID + "' AND " + "Semester = '" + Semester + "' AND " + "Year = '" + Year + "'")
                        print(search)
                        if not valueIsInDB(cur, search):
                            # insert
                            addTakesInsert(cur, StudentID, CID, Semester, Year)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = "Entry already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have four fields: StudentID, CID, Semester, Year")

                elif element == "Chair":
                    try:
                        DID = jsonValue[element][0]['DID']
                        SID = jsonValue[element][0]['SID']
                        search = sqlStatement.format(element, " DID = '" + DID + "'")
                        print(search)
                        if not valueIsInDB(cur, search):
                            # insert
                            addChairInsert(cur, DID, SID)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = "Entry already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have two fields: DID, SID")

                elif element == "CanEnroll":
                    try:
                        SID = jsonValue[element][0]['SID']
                        CID = jsonValue[element][0]['CID']
                        search = sqlStatement.format(element, "SID = '" + SID + "' AND CID = '" + CID + "'")
                        print(search)
                        if not valueIsInDB(cur, search):
                            # insert
                            addCanEnrollInsert(cur, SID, CID)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = "Entry already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have two fields: SID, CID")
                elif element == "Staff":
                    try:
                        SID = jsonValue[element][0]['SID']
                        DID = jsonValue[element][0]['DID']
                        Name = jsonValue[element][0]['Name']
                        Age = jsonValue[element][0]['Age']
                        search = sqlStatement.format(element, "SID = '" + SID + "'")
                        print(search)
                        print("Is it in the db? " + 'str(valueIsInDB(cur, search))')
                        print("After first check in db")
                        if not valueIsInDB(cur, search):
                            # insert
                            addStaffInsert(cur, SID, DID, Name, Age)
                            print("Running in db")
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            print("Error in staff valueIsInDB true")
                            return render_template("insert.html", error = "Entry already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have four fields: SID, DID, Name, Age")
                elif element == "CourseDescription":
                    try:
                        CID = jsonValue[element][0]['CID']
                        Name = jsonValue[element][0]['Name']
                        Credits = jsonValue[element][0]['Credits']
                        search = sqlStatement.format(element, "CID = '" + CID + "'")
                        if not valueIsInDB(cur, search):
                            # insert
                            addCourseDescriptionInsert(cur, CID, Name, Credits)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = "Entry already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have three fields: CID, Name, Credits")
                elif element == "CourseInstance":
                    try:
                        CID = jsonValue[element][0]['CID']
                        Semester = jsonValue[element][0]['Semester']
                        Year = jsonValue[element][0]['Year']
                        SID = jsonValue[element][0]['SID']
                        IsOpen = jsonValue[element][0]['IsOpen']
                        BID = jsonValue[element][0]['BID']
                        RoomNumber = jsonValue[element][0]['RoomNumber']
                        search = sqlStatement.format(element, "CID = '" + CID + "' AND Semester = '" + Semester + "' AND Year = '" + Year + "'")
                        if not valueIsInDB(cur, search):
                            # insert
                            addCourseInstanceInsert(cur, CID, Semester, Year, SID, IsOpen, BID, RoomNumber)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = "Entry already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have seven fields: CID, Semester, Year, SID, IsOpen, BID, RoomNumber")
                elif element == "Professor":
                    try:
                        SID = jsonValue[element][0]['SID']
                        Tenure = jsonValue[element][0]['Tenure']
                        RoomNumber = jsonValue[element][0]['RoomNumber']
                        search = sqlStatement.format(element, "SID = '" + SID + "'")
                        if not valueIsInDB(cur, search):
                            # insert
                            addProfessorInsert(cur, SID, Tenure, RoomNumber)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = "Entry already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have three fields: SID, Tenure, RoomNumber")
                elif element == "Admin":
                    try:
                        SID = jsonValue[element][0]['SID']
                        RoomNumber = jsonValue[element][0]['RoomNumber']
                        search = sqlStatement.format(element, "SID = '" + SID + "'")
                        if not valueIsInDB(cur, search):
                            # insert
                            addAdminInsert(cur, SID, RoomNumber)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = "Entry already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have two fields: SID, RoomNumber")
                elif element == "Building":
                    try:
                        BID = jsonValue[element][0]['BID']
                        DID = jsonValue[element][0]['DID']
                        Name = jsonValue[element][0]['Name']
                        NumRooms = jsonValue[element][0]['NumRooms']
                        search = sqlStatement.format(element, "BID = '" + BID + "'")
                        if not valueIsInDB(cur, search):
                            # insert
                            addBuildingInsert(cur, BID, DID, Name, NumRooms)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = "Entry already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have four fields: BID, DID, Name, NumRooms")
                elif element == "Room":
                    try:
                        BID = jsonValue[element][0]['BID']
                        RoomNumber = jsonValue[element][0]['RoomNumber']
                        Capacity = jsonValue[element][0]['Capacity']
                        search = sqlStatement.format(element, "BID = '" + BID + "' AND RoomNumber = '" + RoomNumber + "'")
                        if not valueIsInDB(cur, search):
                            # insert
                            addRoomInsert(cur, BID, RoomNumber, Capacity)
                            return render_template("insert.html", error = None)
                        else:
                            # ERROR value was already in the database.
                            return render_template("insert.html", error = "Entry already exists in " + element)
                            
                    except:
                        #ERROR  did not have a field did, name, or address
                        return render_template("insert.html", error = "Invalid JSON. You must have three fields: BID, RoomNumber, Capacity")
                else:
                    pass
        
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
        return render_template('view.html', view = rows, queryType = val, run=1)
    except:
        return render_template('view.html', view = None, queriedId = val, queryType = val, run=1)
   
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
        cur.execute("select * from Student s where s.StudentId = '" + val + "'")
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
