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
    students = list()
    i = 0
    while i < size:
        students.append(CreateStudent())
        i += 1
    return students

def DisplayAllStudents(studentList, size):
    for x in studentList:
        print("Student: ", x.name)
        print("Age: ", x.age)
        print("GPA: ", x.gpa)
        print("Grade Level: ", x.gradeLevel)
        print("\n")

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