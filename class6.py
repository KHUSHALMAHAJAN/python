class teacher:
    name = ""
    sub = ""
    def teacher(self):
        self.name = input("Enter a name of teacher")
        self.sub = input("Enter a subject")
class student(teacher):
    stuname = ""
    gread = ""
    def student(self):
        self.stuname = input("Enter a name of student")
        self.gread = input("Enter a gread")
    def display(self):
        print("teacher name is ", name)
        print("subject name is ",sub)
        print("student name is ",stuname)
        print("gread is ",gread)
obj = student()
obj.display()