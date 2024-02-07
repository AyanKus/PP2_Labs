import random

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

def histogram(numbers):
    for num in numbers:
        print('*' * num)

def guess_the_number():
    secret_number = random.randint(1, 20)
    
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    num_guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        num_guesses += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break
