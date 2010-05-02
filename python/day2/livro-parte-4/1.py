"""
>>> q = Quadrado(4)
>>> q.lado
4
>>> q.set_lado(5)
>>> q.lado
5
>>> q.get_lado()
5
>>> q.calcula_area()
25
"""

class Quadrado(object):
    def __init__(self, lado=0):
        super(Quadrado, self).__init__()
        self.lado = lado

    def set_lado(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def calcula_area(self):
        return self.lado ** 2

if __name__ == '__main__':
    import doctest
    doctest.testmod()