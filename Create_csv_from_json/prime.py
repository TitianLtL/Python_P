def gen_primes(start, end):
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            yield num

# Example: print all primes in the range 50..100
for num in gen_primes(50, 100):
    print(num)
