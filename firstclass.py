class Student():
    collage="ACS Collage"#static/class variable
    def __init__(self,name,rollno,marks): # name,rollno,marks are # Local variable
        self.name=name  # self.name self.name,self.marks are Instance variable
        self.rollno=rollno
        self.marks=marks
        print("WEcome to constructer")
    def display(self):
        print("Welcome display method")
        print(f"name of student {self.name} and roll no {self.rollno} and marks {self.marks} and collage name is {self.collage}")

s=Student('Pawan',11,66)
s1=Student('neha',4,59)
s.display()
s1.display()
