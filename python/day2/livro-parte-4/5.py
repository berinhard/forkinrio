#coding: utf-8
"""
5. Implemente um módulo com: 

Uma classe Ponto, com coordenadas x, y e z.
>>> p = Ponto()
>>> hasattr(p, 'x')
True
>>> hasattr(p, 'y')
True
>>> hasattr(p, 'z')
True

Uma classe Linha, com dois pontos A e B, e que calcule o comprimento da linha.
>>> l = Linha(Ponto(), Ponto(1,1,1))
>>> l.comprimento()
1.7320508075688772

Uma classe Triangulo, com dois pontos A, B e C, que calcule o comprimento dos lados e a área.
>>> t = Triangulo(Ponto(), Ponto(1,0,0), Ponto(0,1,0))
>>> t.ladoA
1.0
>>> t.ladoB
1.0
>>> t.ladoC
1.4142135623730951

"""
from math import sqrt

class Ponto(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

class Linha(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def comprimento(self):
        a = (self.p.x, self.p.y, self.p.z)
        b = (self.q.x, self.q.y, self.q.z)
        v = map(lambda t: t[0] - t[1], zip(a,b))
        return sqrt(sum(map(lambda i: i ** 2, v)))

class Triangulo(object):
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r

    @property
    def ladoA(self):
        return Linha(self.p, self.q).comprimento()

    @property
    def ladoB(self):
        return Linha(self.p, self.r).comprimento()

    @property
    def ladoC(self):
        return Linha(self.q, self.r).comprimento()

if __name__ == '__main__':
    import doctest
    doctest.testmod()