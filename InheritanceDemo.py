class A:
    def __init__(self):
        print(" In A Init ")

    def feature1(self):
        print("Feature 1  is working")

    def feature2(self):
        print("Feature 2  is working")


class B(A):

    def __init__(self):
        super(B, self).__init__()  # Calling superclass constructor
        print("in B Init")

    def feature3(self):
        print("Feature 3  is working")

    def feature4(self):
        print("Feature 4  is working")


class C:
    def feature5(self):
        print("Feature 5  is working")

    def feature6(self):
        print("Feature 6  is working")


class D(C):
    def feature7(self):
        print("Feature 7  is working")

    def feature8(self):
        print("Feature 8  is working")


a1 = A()
b1 = B()

d1 = D()
d1.feature7()

