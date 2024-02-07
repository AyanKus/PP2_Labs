def filter_prime(numbers: list):
    is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

    if not numbers:
        return []
    if is_prime(numbers[0]):
        return [numbers[0]] + filter_prime(numbers[1:])
    return filter_prime(numbers[1:])

nums = [ 1, 2, 3, 4, 5, 6, 7]
result = filter_prime(nums)
print(result)