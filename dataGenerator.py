
#!/usr/bin/python

class Department:
	deptCount = 0

   	def __init__(self, DID, Name, Address):
		self.DID = DID
		self.Name = Name
		self.Address = Address
		Department.deptCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\", \"%s\")" % (self.DID, self.Name, self.Address),

	def printInsert(self):
		print "INSERT INTO Department (\n\tDID, Name, Address)\nVALUES"

class Student:
	studCount = 0

   	def __init__(self, StudentID, Name, Year, Major):
		self.StudentID = StudentID
		self.Name = Name
		self.Year = Year
		self.Major = Major
		Student.studCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\", \"%s\", \"%s\")" % (self.StudentID, self.Name, self.Year, self.Major),

	def printInsert(self):
		print "INSERT INTO Student (\n\tStudentID, Name, Year, Major)\nVALUES"

class Staff:
	staffCount = 0

	def __init__(self, SID, DID, Name, Age):
		self.SID = SID
		self.DID = DID
		self.Name = Name
		self.Age = Age
		Staff.staffCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\", \"%s\", %d)" % (self.SID, self.DID, self.Name, self.Age),

	def printInsert(self):
		print "INSERT INTO Staff (\n\tSID, DID, Name, Age)\nVALUES"

class Chair:
	chairCount = 0

	def __init__(self, DID, SID):
		self.SID = SID
		self.DID = DID
		Chair.chairCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\")" % (self.DID, self.SID),

	def printInsert(self):
		print "INSERT INTO Chair (\n\tDID, SID)\nVALUES"

# Generate departments
deptList = []
studList = []
staffList = []
chairList = []
for index in range(0, 100):
	deptList.append(Department('Dept-%d' % (index), 'Department %d' % (index), 'Address %d' % (index)));
	if index == 0:
		deptList[index].printInsert();
	deptList[index].printValue();
	if index != 99:
		print ','
	else:
		print ';'

for index in range(0, 10000):
	studentYear = ''
	if index % 4 == 0: 
		studentYear = 'Freshman'
	elif index % 4 == 1:
		studentYear = 'Sophomore'
	elif index % 4 == 2:
		studentYear = 'Junior'
	else:
		studentYear = 'Senior'
	studList.append(Student('Stud-%d' % (index), 'Student %d' % (index), studentYear, deptList[index%len(deptList)].DID));
	if(index == 0):
		studList[index].printInsert();
	studList[index].printValue();
	if index != 9999:
		print ','
	else:
		print ';'

for index in range(0, 10000):
	staffList.append(Staff('Staff-%d' % (index), deptList[index%len(deptList)].DID, 'Staff %d' % (index), (index%60) + 20));
	if(index == 0):
		staffList[index].printInsert();
	staffList[index].printValue();
	if index != 9999:
		print ','
	else:
		print ';'

for index in range(0, 100):
	chairList.append(Chair(deptList[index%len(deptList)].DID, staffList[index%len(staffList)].SID));
	if index == 0:
		chairList[index].printInsert();
	chairList[index].printValue();
	if index != 99:
		print ','
	else:
		print ';'
