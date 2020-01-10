from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.easy(self.numer, self.denom) == other

    def __repr__(self):
        return self.easy(self.numer, self.denom)

    def __add__(self, other):
        if (self.numer * other.denom + other.numer * self.denom) == 0:
            return '{}/{}'.format(0, 1)
        else:
            return '{}/{}'.format((self.numer * other.denom + other.numer * self.denom), (self.denom * other.denom))

    def __sub__(self, other):
        if (self.numer * other.denom - other.numer * self.denom) == 0:
            return '{}/{}'.format(0, 1)
        else:
            return '{}/{}'.format((self.numer * other.denom - other.numer * self.denom), (self.denom * other.denom))

    def __mul__(self, other):
        up = self.numer * other.numer
        down = self.denom * other.denom
        return self.easy(up, down)

    def __truediv__(self, other):
        return self.easy((self.numer * other.denom), (other.numer * self.denom))

    def __abs__(self):
        return '{}/{}'.format(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return '{}/{}'.format(pow(self.numer, power), pow(self.denom, power))

    def __rpow__(self, base):
        new_base = pow(base, self.numer)
        base = pow(new_base, 1/self.denom)
        return base

    def easy(self, a, b):
        if (a % b) == 0:
            a = a // b
            b = b // b
        elif (b % a) == 0:
            b = b // a
            a = a // a
        if b < 0:
            if a < 0:
                b = abs(b)
                a = abs(a)
            else:
                a = -a
                b = abs(b)
        while ((a % 2) == 0) and ((b % 2) == 0):
            a = a // 2
            b = b // 2
        return '{}/{}'.format(a, b)
