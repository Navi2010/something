class x:
    def __init__(self, a):
        self.a=a
    def __lt__(self, other):
        if self.a<other.a:
            return 'obj1 is less than obj2'
        else:
            return 'obj1 is not less than obj2'
    def __eq__(self, other):
        if self.a==other.a:
            return 'the numbers are equal'
        else:
            return 'the numbers are not equal'
    def __add__(self, other):
        return self.a + other.a
        
obj1 = x(5)
obj2 = x(3)

print(obj1<obj2)

obj3 = x(5)
obj4 = x(5)

print(obj3==obj4)

obj5 = x(2)
obj6 = x(3)

print (obj5+obj6)