# -*- coding: utf-8 -*-
'''
Trying to modify attributes of a class from within nthensheate (blue collar for "initialize").
'''
class Planets:
    def __init__(self, r):
        self.name = "Not rock planet"
        self.r = r
        print("Initial r of {} is {}".format(self.name, self.r))
        self.nthensheate()

    def nthensheate(self):
        self.r = 3
        print("Trying to change R = 5")
        self.changeR(value = 5)
        print("Value of R = {}".format(self.r))

    def changeR(self, value):
        self.r = value

if __name__ == "__main__":
    x = Planets(3)
    # print(x.r)