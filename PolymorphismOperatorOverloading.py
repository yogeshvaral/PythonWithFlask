class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1+ other.m1
        m2 = self.m2+other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        if m1 > m2 :
            return True
        else:
            return False


s1 = Student(10,20)
s2 = Student(20,30)

s3 = s1+s2

print('m1 {} and m2 {}'.format(s3.m1, s3.m2))

if s1>s2 :
    print("S1 wins")
else:
    print("s2 wins")

