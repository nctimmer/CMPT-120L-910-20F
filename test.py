primes = []
for possiblePrime in range(2, 21):
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
    if isPrime:
        primes.append(possiblePrime)