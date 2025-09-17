class Person:
    def __init__(self,name):
        self.name=name

    def invite(self):
        print("Welcome",self.name)

class Profession:
    def __init__(self,professionType):
       self.professionType=professionType
    def professionTypeDisplay(self):
        print("My Profession is ",self.professionType)

class Experience(Person,Profession):
    def __init__(self,name,professionType,experience_years):
       Person.__init__(self,name)
       Profession.__init__(self,professionType)
       self.experience_years=experience_years
    def experienceYearsDisplay(self):
        print("My Experience is ",self.experience_years)




p2 = Experience('Renju','Sr.SDET',16)
p2.invite()
p2.professionTypeDisplay()
p2.experienceYearsDisplay()


