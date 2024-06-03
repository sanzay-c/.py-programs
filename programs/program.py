# this is for testing the programs

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"        


stu = Student(98, 97, 99)
print(stu.percentage)

stu.phy = 86
print(stu.percentage)