#coding: utf-8
"""
cProfile.runctx('listrgb()', globals(), None)
         16646659 function calls in 173.751 CPU seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.763    0.763  173.751  173.751 <string>:1(<module>)
        1  170.800  170.800  172.989  172.989 <string>:1(listrgb)
 16581375    1.945    0.000    1.945    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    65281    0.244    0.000    0.244    0.000 {range}

cProfile.runctx('genrgb()', globals(), None)
         16581378 function calls in 171.993 CPU seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.762    0.762  171.993  171.993 <string>:1(<module>)
        1  169.367  169.367  171.231  171.231 <string>:9(genrgb)
 16581375    1.864    0.000    1.864    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

def listrgb():
    cores = []
    for red in range(255):
        for green in range(255):
            for blue in range(255):
                cores.append((red, green, blue))
    return cores

def genrgb():
    cores = []
    for red in xrange(255):
        for green in xrange(255):
            for blue in xrange(255):
                cores.append((red, green, blue))
    return cores

if __name__ == '__main__':
    import cProfile
    cProfile.runctx('listrgb()', globals(), None)
    cProfile.runctx('genrgb()', globals(), None)

