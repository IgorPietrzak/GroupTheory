from math import gcd

# This is a multiplicative group of integers modulo n

class Zn:
    def __init__(self, number):
        self.number = number
        self.order = len(self.make())

    def make(self):
        zn = []
        for i in range(0,self.number):
            if gcd(i,self.number) == 1:
                zn.append(i)
        return zn
        
    def e_order(self, x):
        if x == 1:
            return 1
        order = 0
        for i in range(-10,11,1):
            if x**i in self.make():
                order += 1

        return order

    def orders(self):
        for i in self.make():
            print(f"Order({i}): " + str(self.e_order(i)))
            print("--------------")
    
