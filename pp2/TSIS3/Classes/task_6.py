def IsPrime(num: int):
    diver = 2

    if num < 2:
        return False

    while num % diver != 0:
        diver += 1

    return diver == num

nums = { 1, 2, 3, 4, 5, 6, 7 }
PrimeNumbers = lambda x: list(filter(IsPrime, x))

print(f"Func IsPrime(): {PrimeNumbers(nums)}")

# Or

is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
result_prime_list = list(filter(is_prime, nums))

print(f"Anonym Func Prime(): {result_prime_list}")