class Test:
    x=100 #class attribute
    __y=500 #hidden class attribute
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.__hello = a+" "+b
        # print("Object Initialised with value {}".format(self.a)) #intializer statement
    @property #now this function can be called without closed brackets
    def full_name(self):
        return self.a+" "+self.b
    @classmethod #this is for calling hidden class attributes
    def get_y(cls):
        return cls.__y
    def __increment(self):
        self.c+=10
        return self.c
    def this_increment(self):
        return self.__increment()
    @staticmethod 
    def greet():
        return "Hello Bae"
    def return_y(self):
        if self.c >= 100:
            raise ValueError("Unexpected value haha ")
        else:
            return self.c
a = Test("Gauransh","Soni",10)
# print(a.full_name)
# print(a._Test__hello) #this can access the __hello attribute
# print(a.this_increment())
print(a.return_y())