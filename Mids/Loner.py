def findloner(numbers):
    loner = 0
    for num in numbers:
        loner ^= num

    print(loner)

findloner([2,4,4,6,6,9,9,2,7])