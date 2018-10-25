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
        students_titlecase= student['name'].title()
    return students_titlecase


def print_studens_titlecase():
    students_titlecase= get_students_titlecase()
    print (students_titlecase)


def add_student(student_name, student_id):
    student={
        "name": student_name,
        "id": student_id
    }
    students.append(student)

student_name= input("Student name: ")
student_id= input("Student ID: ")

add_student(student_name, student_id)
print_studens_titlecase()