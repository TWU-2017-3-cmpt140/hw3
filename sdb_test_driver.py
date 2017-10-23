#*******************************************************************************
# CMPT 140 Assignment #3
# sdb test driver - shows some usage of the classes in sdb
#*******************************************************************************
import sdb

# create a database of students
db = {}
db[11111] = sdb.Student(11111,"Andrian","Anderson","1980-12-10")
db[22222] = sdb.Student(22222,"Betty","Baker","1995-02-10")
db[33333] = sdb.Student(33333,"Carlos","Chan","1999-03-28")
db[44444] = sdb.Student(44444,"David","Duncan","1986-01-23")

# add courses to students
cmpt140 = sdb.Course("CMPT140",sdb.Schedule())
cmpt140.schedule.events.add(sdb.Event(sdb.WeekDay.MONDAY,8,9))
cmpt140.schedule.events.add(sdb.Event(sdb.WeekDay.WEDNESDAY,8,9))
cmpt140.schedule.events.add(sdb.Event(sdb.WeekDay.FRIDAY,8,9))
biol103 = sdb.Course("BIOL103",sdb.Schedule())
biol103.schedule.events.add(sdb.Event(sdb.WeekDay.MONDAY,10,11))
biol103.schedule.events.add(sdb.Event(sdb.WeekDay.WEDNESDAY,10,11))
biol103.schedule.events.add(sdb.Event(sdb.WeekDay.FRIDAY,10,11))
chem101 = sdb.Course("CHEM101",sdb.Schedule())
chem101.schedule.events.add(sdb.Event(sdb.WeekDay.MONDAY,10,11))
chem101.schedule.events.add(sdb.Event(sdb.WeekDay.WEDNESDAY,10,11))
chem101.schedule.events.add(sdb.Event(sdb.WeekDay.FRIDAY,10,11))

for stNum, student in db.items():
    student.addCourse(cmpt140)
    student.addCourse(biol103)

for stNum, s in db.items():
    print(s)
    for c in s.courses:
        print(c)
    print("")
