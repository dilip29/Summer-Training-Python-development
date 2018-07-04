class employee:
    def __init__(self,a):
        self.salary=a

    def sal(self):
        return self.salary


class salesman(employee):
    def __init__(self,a,b):
        super().__init__(a)
        self.inct=b

    def sal(self):
        return self.salary + self.inct


e1=employee(8400)
print(e1.sal())
e2=salesman(7800,1000)
print(e2.sal())

        
