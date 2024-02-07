def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

user_input = input("Enter sentence: ")
reversed_sentence = reverse_sentence(user_input)
print("Sentence with inverted words:", reversed_sentence)
