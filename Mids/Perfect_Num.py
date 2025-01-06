def divisors(n):
    divisor = []
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
            divisor_sum += i
    divisor.append(n)
    divisor.sort()
    divisor_sum += n
    print("Divisors: ", ", ".join(map(str,divisor)))
    print("Divisor sum: ", divisor_sum)
    return divisor_sum

def divisors_sum(n):
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    divisor_sum += n
    return divisor_sum

def p2(n):
    p2_num = []
    for i in range(1,n):
        a = divisors_sum(i)
        if a == 2 * i:
            p2_num.append(i)

    print("Doubly Perfect Numbers below 10000: ", ", ".join(map(str,p2_num)) )
    return p2

def pm(n):
    pm = []
    for i in range(1, n):
        divisor_sum = divisors_sum(i)

        if divisor_sum % i == 0:
            multiple = divisor_sum // i
            pm.append((i, multiple))
    print("Multiply Perfect Numbers below 50000: ", ", ".join(map(str,pm)) )
    return pm

divisors(6)
p2(10000)
pm(50000)