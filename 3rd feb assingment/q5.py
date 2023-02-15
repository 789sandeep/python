# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
# first 20 prime numbers.
def generator_prime_number():
    primes = []
    for num in range(2, 1001):
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
a=generator_prime_number()
for number in range(20):
    print(next(a))       