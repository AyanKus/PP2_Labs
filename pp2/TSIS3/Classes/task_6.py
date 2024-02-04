def IsPrime(num: int):
    diver = 2

    if num < 2:
        return False

    while num % diver != 0:
        diver += 1

    return diver == num

nums = { 1, 2, 3, 4, 5, 6, 7 }
PrimeNumbers = lambda x: list(filter(IsPrime, x))

print(PrimeNumbers(nums))