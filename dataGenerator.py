
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

class Takes:
	takesCount = 0

   	def __init__(self, StudentID, CID, Semester, Year):
		self.StudentID = StudentID
		self.CID = CID
		self.Semester = Semester
		self.Year = Year
		Takes.takesCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\", \"%s\", \"%s\")" % (self.StudentID, self.CID, self.Semester, self.Year),

	def printInsert(self):
		print "INSERT INTO Takes (\n\tStudentID, CID, Semester, Year)\nVALUES"

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

class CourseDescription:
	courseCount = 0

   	def __init__(self, CID, Name, Credits):
		self.CID = CID
		self.Name = Name
		self.Credits = Credits
		CourseDescription.courseCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\", %d)" % (self.CID, self.Name, self.Credits),

	def printInsert(self):
		print "INSERT INTO CourseDescription (\n\tCID, Name, Credits)\nVALUES"

class CourseInstance:
	courseCount = 0

   	def __init__(self, CID, Semester, Year, SID, IsOpen, BID, RoomNumber):
		self.CID = CID
		self.Semester = Semester
		self.Year = Year
		self.SID = SID
		self.IsOpen = IsOpen
		self.BID = BID
		self.RoomNumber = RoomNumber
		CourseInstance.courseCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\", \"%s\", \"%s\", %d,  \"%s\", \"%s\")" % (self.CID, self.Semester, self.Year, self.SID, self.IsOpen, self.BID, self.RoomNumber),

	def printInsert(self):
		print "INSERT INTO CourseInstance (\n\tCID, Semester, Year, SID, IsOpen, BID, RoomNumber)\nVALUES"

class Building:
	buildingCount = 0

	def __init__(self, BID, DID, Name, NumRooms):
		self.BID = BID
		self.DID = DID
		self.Name = Name
		self.NumRooms = NumRooms
		Building.buildingCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\", \"%s\", %d)" % (self.BID, self.DID, self.Name, self.NumRooms),

	def printInsert(self):
		print "INSERT INTO Building (\n\tBID, DID, Name, NumRooms)\nVALUES"

class Room:
	roomCount = 0

   	def __init__(self, BID, RoomNumber, Capacity):
		self.BID = BID
		self.RoomNumber = RoomNumber
		self.Capacity = Capacity
		Room.roomCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\", %d)" % (self.BID, self.RoomNumber, self.Capacity),

	def printInsert(self):
		print "INSERT INTO Room (\n\tBID, RoomNumber, Capacity)\nVALUES"

class Professor:
	profCount = 0

   	def __init__(self, SID, Tenure, RoomNumber):
		self.SID = SID
		self.Tenure = Tenure
		self.RoomNumber = RoomNumber
		Professor.profCount += 1

	def printValue(self):
		print "(\"%s\", %d, \"%s\")" % (self.SID, self.Tenure, self.RoomNumber),

	def printInsert(self):
		print "INSERT INTO Professor (\n\tSID, Tenure, RoomNumber)\nVALUES"

class Admin:
	adminCount = 0

   	def __init__(self, SID, RoomNumber):
		self.SID = SID
		self.RoomNumber = RoomNumber
		Admin.adminCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\")" % (self.SID, self.RoomNumber),

	def printInsert(self):
		print "INSERT INTO Admin (\n\tSID, RoomNumber)\nVALUES"

class CanEnroll:
	canEnrollCount = 0

   	def __init__(self, SID, CID):
		self.SID = SID
		self.CID = CID
		CanEnroll.canEnrollCount += 1

	def printValue(self):
		print "(\"%s\", \"%s\")" % (self.SID, self.CID),

	def printInsert(self):
		print "INSERT INTO CanEnroll (\n\tSID, CID)\nVALUES"

# Generate departments
deptList = []
studList = []
staffList = []
chairList = []
courseDescList = []
courseInstList = []
buildingList = []
roomList = []
profList = []
adminList = []
takesList = []
enrollList = []
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

for index in range(0, 10000):
	courseDescList.append(CourseDescription('%s-%d' % (deptList[index%len(deptList)].DID, index), 'Course %d' % (index), (index%4) + 1));
	if(index == 0):
		courseDescList[index].printInsert();
	courseDescList[index].printValue();
	if index != 9999:
		print ','
	else:
		print ';'

for index in range(0, 100):
	buildingList.append(Building('B-%d' % (index), deptList[index%len(deptList)].DID, 'Building %d' % (index), index+100));
	if index == 0:
		buildingList[index].printInsert();
	buildingList[index].printValue();
	if index != 99:
		print ','
	else:
		print ';'

for index in range(0, 10000):
	roomList.append(Room(buildingList[index%len(buildingList)].BID, index, (index%200) + 20));
	if(index == 0):
		roomList[index].printInsert();
	roomList[index].printValue();
	if index != 9999:
		print ','
	else:
		print ';'

for index in range(0, 100):
	profList.append(Professor(staffList[index%len(staffList)].SID, index%2, roomList[index%len(roomList)].RoomNumber));
	if index == 0:
		profList[index].printInsert();
	profList[index].printValue();
	if index != 99:
		print ','
	else:
		print ';'

for index in range(0, 100):
	adminList.append(Admin(staffList[(index+100)%len(staffList)].SID,roomList[(index+100)%len(roomList)].RoomNumber));
	if index == 0:
		adminList[index].printInsert();
	adminList[index].printValue();
	if index != 99:
		print ','
	else:
		print ';'

for index in range(0, 10000):
	semester = ''
	if index % 2 == 0:
		semester = 'FALL'
	else:
		semester = 'SPRING'
	courseInstList.append(CourseInstance(courseDescList[index%len(courseDescList)].CID, semester, (index%4) + 2014,
		profList[index%len(profList)].SID, index%2, roomList[index%len(roomList)].BID, roomList[index%len(roomList)].RoomNumber));
	if(index == 0):
		courseInstList[index].printInsert();
	courseInstList[index].printValue();
	if index != 9999:
		print ','
	else:
		print ';'

for index in range(0, 10000):
	takesList.append(Takes(studList[index%len(studList)].StudentID, courseInstList[index%len(courseInstList)].CID,
		courseInstList[index%len(courseInstList)].Semester, courseInstList[index%len(courseInstList)].Year));
	if(index == 0):
		takesList[index].printInsert();
	takesList[index].printValue();
	if index != 9999:
		print ','
	else:
		print ';'

for index in range(0, 100):
	enrollList.append(CanEnroll(profList[index%len(profList)].SID, courseInstList[index%len(courseInstList)].CID));
	if index == 0:
		enrollList[index].printInsert();
	enrollList[index].printValue();
	if index != 99:
		print ','
	else:
		print ';'