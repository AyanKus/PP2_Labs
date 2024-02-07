from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    
    for perm in perms:
        print(''.join(perm))
        i += 1

user_input = input("Enter the string: ")
print("All permutations of the string:")
print_permutations(user_input)
