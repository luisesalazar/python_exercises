students=[]

class Student:

    school_name= "Springfield Elementary"


    #constructor
    def __init__(self, student_name, student_id=1):
        self.name= student_name
        self.id= student_id
        students.append(self)


    #when you print an Student instance
    def __str__(self):
        return "Student " + self.name


    def get_name_capitalize(self):
        return self.name.capitalize()


    def get_school_name(self):
        return self.school_name

#inheritance
class HighSchoolStudent(Student):
    #overrides the attribute
    school_name = "Springfield High School"

    #polymorphism
    def get_name_capitalize(self):
        return super().get_name_capitalize() + "HS"


    def get_school_name(self):
        return self.school_name


mark= Student("Mark")

print (mark)

erick= HighSchoolStudent("Erick")

print(erick)