def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

# Example usage
input_word = input("Enter a word or phrase: ")
if is_palindrome(input_word):
    print(input_word, "is a palindrome!")
else:
    print(input_word, "is not a palindrome.")
