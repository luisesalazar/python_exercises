#pass multiple parameters
def print_args(val, **kwargs):
    print (val)
    print (kwargs['name'])

print_args("hello", name="luis", lastname="Salazar")

#app
students=[]

def get_students_titlecase():
    students_titlecase=[]
    for student in students:
        students_titlecase.append(student['name'].title())
    return students_titlecase


def print_studens_titlecase():
    students_titlecase= get_students_titlecase()
    print (students_titlecase)


def add_student(student_name, student_id=1):
    student={
        "name": student_name,
        "id": student_id
    }
    students.append(student)


def read_file():
    try:
        students_file= open("students.txt", "r")

        for student in read_students(students_file):
            add_student(student)

        students_file.close()

    except Exception as ex:
        print(ex)

#yield
def read_students(f):
    for line in f:
        yield line

def save_file(student):
    try:
        students_file = open("students.txt", "a")
        students_file.write(student + "\n")
        students_file.close()

    except Exception as ex:
        print(ex)


read_file()
print_studens_titlecase()

student_name= input("Student name: ")
student_id= input("Student ID: ")

add_student(student_name, student_id)
save_file(student_name)
