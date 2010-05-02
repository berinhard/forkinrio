#coding: utf-8
"""
Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
>>> c = Carro(10)
>>> hasattr(c, 'litros_combustivel')
True
>>> hasattr(c, 'km_por_litro')
True

O consumo é especificado no construtor e o nível de combustível inicial é 0.
>>> c = Carro(10)
>>> c.litros_combustivel
0
>>> c.km_por_litro
10

Forneça um método mover(km) que receba a distância em quilômetros e reduza o nível de combustível no tanque de gasolina.
>>> c = Carro(10)
>>> c.litros_combustivel = 2
>>> c.mover(10)
>>> c.litros_combustivel
1
>>> c.mover(20)
Traceback (most recent call last):
...
OutOfGasException

Forneça um método  gasolina(),  que retorna o nível  atual  de combustível.
>>> c = Carro(10)
>>> c.gasolina()
0

Forneça um método abastecer(litros), para abastecer o tanque.
>>> c = Carro(10)
>>> c.abastecer(1)
>>> c.litros_combustivel
1
"""

class OutOfGasException(Exception):
    pass

class Carro(object):
    litros_combustivel = 0
    km_por_litro = 0

    def __init__(self, km_por_litro=0):
        self.km_por_litro = km_por_litro

    def mover(self, km):
        self.litros_combustivel -= km / self.km_por_litro
        
        if self.litros_combustivel < 0:
            self.litros_combustivel = 0
            raise OutOfGasException()

    def abastecer(self, litros):
        self.litros_combustivel += abs(litros)

    def gasolina(self):
        return self.litros_combustivel


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    