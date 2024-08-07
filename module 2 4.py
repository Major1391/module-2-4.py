numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
NotPrimes = []
index = 0

for i in numbers:
    if i == 1:
        continue
    for j in range(1, i+1):
        if i % j == 0:
            index += 1
    if index == 2:
        Primes.append(i)
    else:
        NotPrimes.append(i)
    index = 0
print(Primes)
print(NotPrimes)