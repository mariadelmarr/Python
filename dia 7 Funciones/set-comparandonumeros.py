# Practica de sets interseccion de pares, impares, primos y compuestos

# primes = set([]) o {}
primes = {2, 3, 5, 7} #primos
composites = {4, 6, 8, 9, 10} #compuestos
evens = {2, 4, 6, 8, 10} #pares
odds = {1, 3, 5, 7, 9} #impares

print( primes.intersection(composites))
print( primes.intersection(evens))
print( primes.intersection(odds))

print( primes.difference(composites))
print( composites.difference(primes))
print( primes.difference(evens))
print( primes.difference(odds))
