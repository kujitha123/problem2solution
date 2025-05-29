class Father:
    def fun1(self):
        print("head of family")
class daughter1(Father):
    def fun2(self):
        print("first children")
class daughter2(Father):
    def fun3(self):
        print("second children")
ob = daughter2()
ob.fun1()
ob.fun3()
ob = daughter1()
ob.fun1()



