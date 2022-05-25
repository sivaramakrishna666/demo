class A:
    def __init__(self):
        print("these is class A")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
    def mul(self,i=None,j=None,k=None):
        h=0
        if i != None and j != None and k != None:
            h= i*j*k
        elif i != None and j != None:
            h=i*j
        else:
            h=i
class B:
    def __init__(self):
        print("these is class B")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
class C(A,B): ##A and B are supercalsses for C
    def feature5(self):
        super().__init__()## Method resolution order
        super(B, self).feature4()
        print("feature 5 is working")

a1=A()
b1=B()
c1=C()
c2=B()


