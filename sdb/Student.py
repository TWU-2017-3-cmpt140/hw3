#*******************************************************************************
# CMPT 140 Assignment #3
# Class Student definition file
#*******************************************************************************
import datetime
class Student:
    """
    fields:
        studentNumber
        firstName
        lastName
        birthDate
        courses - set of Course objects
    """

    #***************************************************************************
    # Class initializer
    # this function creates a Student object
    #
    # input: studentNumber, firstName, lastName, birthDate
    def __init__(self, studentNumber, firstName, lastName, birthDate):
        self.studentNumber = studentNumber
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.courses = set() # let courses be a set

    #***************************************************************************
    # define criteria for equality
    #
    # input: object to compare
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.studentNumber == other.studentNumber
        return NotImplemented # indicate that you cannot compare Student
                              # object with instance of other classes


    #***************************************************************************
    # returns a string representation of this instance
    #
    # returns: a string
    def __str__(self):
        return self.lastName+", "+self.firstName+\
    " ("+str(self.studentNumber)+")"

    #***************************************************************************
    # getAge() calculate age of student
    #
    # returns an integer representing the age
    def getAge(self):
        now = datetime.datetime.now() # current date
        return int((b-a).days/365)

    #***************************************************************************
    # add the specified course
    #
    # return True if courses added successfully, otherwise False
    def addCourse(self, course):
        if not (course in self.courses):
            self.courses.add(course)
            return True
        else:
            return False # student already registered for this course

    #***************************************************************************
    # remove the specified course
    #
    # return True if courses removed successfully, otherwise False
    def removeCourse(self, course):
        if course in self.courses:
            self.courses.remove(course)
            return True
        else:
            return False # student not registered for this course

    #***************************************************************************
    # check to see if the input course creates conflicts with any registered
    # courses
    #
    # can assume
    #     1. all courses will be between 8am-6pm.
    #     2. all classes starts either on the hour or 30 minutes afte the hour
    #        (e.g. 13:30, 14:30).
    #     3. all clases are either 1 hour long or 1.5 hours long.
    #
    # returns True if there is conflict, False otherwise
    def conflictWith(self, course):
        pass

    #***************************************************************************
    # list the courses the student is currently enrolled in
    #
    # returns a list of Course objects
    def listCourses(self):
        pass

    #***************************************************************************
    # print this student's time table to the console
    #
    # can assume all course names are 7 characters long e.g. CMPT140
    #
    # example output:
    #
    #       MONDAY   TUESDAY  WEDNESDAY  THURSDAY  FRIDAY
    # 08:00 CMPT140           CMPT140              CMT140
    # 08:30 CMPT140           CMPT140              CMT140
    # 09:00
    # 09:30
    # 10:00          BIOL103             BIOL103
    # 10:30          BIOL103             BIOL103
    # 11:00          BIOL103             BIOL103
    # 11:30
    # 12:00
    # 12:30
    # 13:00 MATH101           MATH101              MATH101
    # 13:30 MATH101           MATH101              MATH101
    # 14:00
    # 14:30
    # 15:00
    # 15:30
    # 16:00
    # 16:30
    # 17:00
    # 17:30
    # 18:00
    #
    # returns None
    def printTimeTable(self):
        pass
