from student import Student


#inheritance
class HighSchoolStudent(Student):
    #overrides the attribute
    school_name = "Springfield High School"

    #polymorphism
    def get_name_capitalize(self):
        return super().get_name_capitalize() + "HS"


    def get_school_name(self):
        return self.school_name