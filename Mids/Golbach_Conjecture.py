def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def prime_numbers(maxn):
    num = []
    for i in range(1, maxn+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            num.append(str(i))
    print("Prime Numbers: ", ", ".join(num))

def goldbach_conjecture(maxn):
    print("Checking Goldbach Conjecture for even numbers up to", maxn)
    for n in range(4, maxn + 1, 2):
        found_prime_pair = False
        for p in range(2, n):
            if not isprime(p):
                continue
            complement = n - p
            if isprime(complement):
                print(f"{n} = {p} + {complement}")
                found_prime_pair = True
                break
        if not found_prime_pair:
            print(f"Goldbach Conjecture fails for {n}")
            return False
    print("Goldbach Conjecture holds for all even numbers up to", maxn)
    return True
def prime_pairs(n):
    if n % 2 != 0 or n <= 2:
        return []
    primes = [num for num in range(2, n + 1) if isprime(num)]
    prime_pairs = []

    for p in primes:
        if p >= n:
            break
        complement = n - p
        if isprime(complement) and p <= complement:
            prime_pairs.append((p, complement))

    print(f"Prime Pairs of {n} = ", " = ".join(f"{pair[0]} + {pair[1]}" for pair in prime_pairs))


isprime(91)
prime_numbers(100)
goldbach_conjecture(100)
prime_pairs(100)