# encoding: utf-8

def celsius_to_farenheit(celsius):
    if not isinstance(celsius, float):
        raise TypeError("Float temperature expected")
    return 32.0 + (9.0 / 5.0) * celsius

def farenheit_to_celsius(farenheit):
    if not isinstance(farenheit, float):
        raise TypeError("Float temperature expected")
    return (farenheit - 32.0) / (9.0 / 5.0)

def trial_division(n):
    from math import sqrt
    
    if n <= 1:
        return False # Primes starts on 2
    
    # Caso especial da porra
    if n == 2:
        return True

    # Numeros pares > 2 nao sao primos
    if n % 2 == 0:
        return False

    square_root = int(sqrt(n))
    for m in range(3, square_root + 1, 2): # lista de nums impares ate sqrt
        if n % m == 0:
            return False
    return True

def flat_list(list_with_lists):
    flat = []
    for i in lists_with_lists:
        flat.extend(i)
    return flat

def calc_dict(operands):
    values = operands.values()
    total = sum(values)
    avg = total / len(values)
    vary = max(values) - min(values)
    return total, avg, vary

def mirror_words(sentence):
    mirror = lambda w: w[::-1]
    words = sentence.split()
    return ' '.join(map(mirror, words))

def ordena(dados, chave=0, reverso=False):
    return sorted(dados, 
                  key=lambda t: t[chave],
                  reverse=reverso)

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print 'ordena dados'
  test(ordena([(3,3), (2,2), (1,1)]), [(1,1), (2,2), (3,3)])
  test(ordena([(2,4), (1,3), (3,1)], 1), [(3,1), (1,3), (2,4)])
  test(ordena([(2,4), (1,3), (3,1)], 1, True), [(2,4), (1,3), (3,1)])
  test(ordena([(3,3), (2,2), (1,1)], 1, True), [(3,3), (2,2), (1,1)])

  print 'mirror words in sentence'
  test(mirror_words("abc"), "cba")
  test(mirror_words("abc def"), "cba fed")
  test(mirror_words("abc def ghi"), "cba fed ihg")

  print 'celsius para farenheit'
  test(celsius_to_farenheit(0.0), 32.0)
  test(celsius_to_farenheit(40.0), 104.0)
  test(celsius_to_farenheit(-10.0), 14.0)

  print 'farenheit para celsius'
  test(farenheit_to_celsius(32.0), 0.0)
  test(farenheit_to_celsius(104.0), 40.0)
  test(farenheit_to_celsius(14.0), -10.0)

  print 'verifica se um numero e primo'
  test(trial_division(1), False)
  test(trial_division(2), True)
  test(trial_division(4), False)
  test(trial_division(17), True)
  test(trial_division(97), True)
  test(trial_division(100), False)
  
  print 'calcula soma, media, max, min'
  test(calc_dict({'a': 1, 'b': 2, 'c': 3}), (6, 2, 2))
  test(calc_dict({'a': 3, 'b': 2, 'c': 1}), (6, 2, 2))
  test(calc_dict({'a': 2, 'b': 3, 'c': 5}), (10, 3, 3))

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()