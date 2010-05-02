"""
>>> l = [1, 1, 2, 2, 3, 4, 5, 5]
>>> u = UniqueList(l)
>>> u.unique()
[1, 2, 3, 4, 5]
"""

class UniqueList(list):
    def __init__(self, values=[]):
        super(UniqueList, self).__init__()
        self.values = values

    def unique(self):
        u = []
        for i in self.values:
            if i not in u:
                u.append(i)
        return u

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    