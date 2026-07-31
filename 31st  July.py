# CLASS
#1 
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


s = student("sru", 20)
s.display()
