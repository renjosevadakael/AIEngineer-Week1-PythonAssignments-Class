class Person:
    def __init__(self,name):
        self.name=name
    def invite(self):
        print("Welcome ", self.name)

p1=Person("Renju")
p2=Person("Jeoge")

p1.invite()
p2.invite()