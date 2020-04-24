class Fraction:
    def __init__(self,name):
        try:
            num = float(name)
        except:
            for i in name :
                if i=='/' :
                    index = name.index(i)
                    num = float(name[:index]) / float(name[index+1:])
        self.name = num 
    def __add__(self,other):
        total = self.name + other.name
        return round(total,5)
    def __sub__(self,other):
        total = self.name - other.name
        return round(total,5)
    def __mul__(self,other):
        if self.name ==0 or other.name ==0:
            return 0.0
        else :
            total = self.name * other.name
            return round(total,5)
    def __truediv__(self,other):
        try:
            total = self.name / other.name
            return round(total,5)
        except:
            return "division not possible"
    def __eq__(self,other):
        return self.name == other.name
        """elif self.name == other.name:
            return True
        else:
            return False"""
    def __lt__(self,other):
        if self.name < other.name:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.name>other.name:
            return True
        else:
            return False
    def __le__(self,other):
        if self.name<=other.name:
            return True
        else:
            return False
    def __ge__(self,other):
        if self.name>=other.name:
            return True
        else:
            return False
    def __ne__(self,other):
        if self.name!=other.name:
            return True
        else:
            return False
    def __abs__(self):
        ans = Fraction(abs(self.name))
        return round(ans.name,5)
if __name__ == '__main__':
    a, b = input().split(" ")

    fraction_1 = Fraction(a)
    fraction_2 = Fraction(b)

    print("add:", fraction_1 + fraction_2)
    print("sub:", fraction_1 - fraction_2)
    print("mul:", fraction_1 * fraction_2)
    print("div:", fraction_1 / fraction_2)
    print("==:", fraction_1 == fraction_2)
    print("<:", fraction_1 < fraction_2)
    print(">:", fraction_1 > fraction_2)
    print("<=:", fraction_1 <= fraction_2)
    print(">=:", fraction_1 >= fraction_2)
    print("!=:", fraction_1 != fraction_2)
    print("abs_1:", abs(fraction_1))
    print("abs_2:", abs(fraction_2))
    print("abs eql:", abs(fraction_1) == fraction_1.name)