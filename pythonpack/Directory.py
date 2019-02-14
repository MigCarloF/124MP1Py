from pip._vendor.distlib.compat import raw_input

from pythonpack.Student import Student


def Directory():
    # Displays title
    Title()

    # gets number of students
    numOfStudents = int(raw_input("Input nubmer of students to store: "))

    # creates students
    students = CreateStudents(numOfStudents)

    # displays students
    DisplayAllStudents(students, numOfStudents)

def CreateStudents(size):
    pass

def DisplayAllStudents(studentList, size):
    pass

def Title():
    print("Student Directory Storage\n")

def CreateStudent():
    # gets details of student to return
    print("Creating new student...\n")
    name = raw_input("Input name: ")
    age = raw_input("Input age: ")
    gpa = raw_input("Input gpa: ")
    gradeLevel = raw_input("Input grade level: ")
    print("\n")
    return Student(name, age, gpa, gradeLevel)