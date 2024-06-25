import fractions

fracs = input().split()

def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i == 0 and b%i == 0:
            return i
            break

class Fraction:
    def __init__(self,num,den):
        self.num = int(num)
        self.den = int(den)

    def __add__(self,other):
        newnum = self.num*other.den+other.num*self.den
        newden = self.den*other.den
        commcn = gcd(newnum,newden)
        return Fraction(newnum/commcn,newden/commcn)

    def __str__(self):
        return str(self.num)+'/'+str(self.den)


f1 = Fraction(fracs[0],fracs[1])
f2 = Fraction(fracs[2],fracs[3])
f3 = f1 + f2

print(str(f3))