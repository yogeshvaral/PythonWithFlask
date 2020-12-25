class Computer:

    def __init__(self, model, ram):
        self.model = model
        self.ram = ram

    def config(self):
        print("i5,16gb,1TB")
        print("Model and ram is", self.model, self.ram)


comp1 = Computer("AMD", 16)
comp2 = Computer("i5", 24)

comp1.config()
comp2.config()


class Person:
    def __init__(self):
        self.name = "Yogesh"
        self.age = 32

    def updateAge(self):
        self.age = 22

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


p1 = Person()
p2 = Person()
# p1.updateAge()
print(p1.name, p1.age)
print(p2.name, p2.age)

if p1.compare(p2):
    print("They are same")
else:
    print("They are different")


class Car:
    wheels = 4  # claas level variable in Class  Namespace

    def __init__(self):
        # Instance level variables in Instance Name space
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

Car.wheels = 6

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)


class Student:
    school = "SIT"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def getAvg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getschoolinfo(cls):
        return cls.school
    @staticmethod
    def getInfo():
        print("This is student class")


s1 = Student(12, 13, 14)
s2 = Student(23, 45, 56)

print(s1.getAvg())
print(s2.getAvg())
print(Student.getschoolinfo())
Student.getInfo()