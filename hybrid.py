class A:
    def fun1(self):
        print("Class A")
class B(A):
    def fun2(self):
        print("Class B")
class C(A):
    def fun3(self):
        print("Class C")
class D(B, C):
    def fun4(self):
        print("Class D")
ob = D()  
ob.fun1()  
ob.fun2()
ob.fun3()
ob.fun4()


