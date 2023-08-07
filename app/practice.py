

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("hii",self.name)
        print("u r marks is",self.marks)
    def grade(self):
        if self.marks>60:
            print("u r pass")
        else:
            print("u r fail")

n=int(input("enter the no of students:"))
for i in range(n):
    name=input("enter u r name:")
    marks=int(input("enter u r marks:"))
    c=Student(name,marks)
    c.display()
    c.grade()
    print()