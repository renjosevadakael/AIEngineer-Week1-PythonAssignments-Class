class Person:
    def __init__(self,name):
        self.name=name

    def invite(self):
        print("Welcome",self.name)

class Profession(Person):
    def __init__(self,name,professionType):
        super().__init__(name)
        self.professionType=professionType
    def professionTypeDisplay(self):
        print("My Profession is ",self.professionType)

class Experience(Profession):
    def __init__(self,name,professionType,experience_years):
        super().__init__(name,professionType)
        self.experience_years=experience_years
    def experienceYearsDisplay(self):
        print("My Experience is ",self.experience_years)

p1 = Profession('Mani','Director')
p1.invite()
p1.professionTypeDisplay()


p2 = Experience('Renju','Sr.SDET',16)
p2.invite()
p2.professionTypeDisplay()
p2.experienceYearsDisplay()


