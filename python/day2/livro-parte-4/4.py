#coding: utf-8
"""
Implementar uma classe Vetor:
>>> v1 = Vetor(1, 2, 3)
>>> v2 = Vetor(3, 2, 1)

Com coordenadas x, y e z. 
>>> hasattr(v1, 'x')
True
>>> hasattr(v1, 'y')
True
>>> hasattr(v1, 'z')
True

Que suporte soma
>>> v1 + v2
<Vetor (x=4, y=4, z=4)>

Que suporte subtração
>>> v1 - v2
<Vetor (x=-2, y=0, z=2)>

Que suporte produto escalar
>>> v1.scalar(v2)
10

Que suporte produto vetorial.
>>> v1 * v2
<Vetor (x=-4, y=8, z=-4)>

Que calcule o módulo (valor absoluto) do vetor.
>>> v1.modulo()
3.7416573867739413
"""
from math import sqrt

class Vetor(object):
    def __init__(self, x, y, z):
        super(Vetor, self).__init__()
        self.x, self.y, self.z = x, y ,z

    def __repr__(self):
        return "<%s (x=%s, y=%s, z=%s)>" % (
            self.__class__.__name__, 
            self.x, self.y, self.z)

    def modulo(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vetor(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vetor(x, y, z)

    def scalar(self, other):
        a = (self.x, self.y, self.z)
        b = (other.x, other.y, other.z)
        return sum(map(lambda t: t[0] * t[1], zip(a,b)))

    def __mul__(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vetor(x, y, z)

if __name__ == '__main__':
    import doctest
    doctest.testmod()