# Description: You are given a first name and a last name of a person on two
#  different lines. Output the following with the name:
#   Hello firstname lastname! You just delved into python.
# Sample Input : abracadabra
#                5 k
# Sample Output : abrackdabra

# Define the mutate function used to modify the string
def mutate_string(string, position, character):
    # Use string concatenation
    mutated_string = string[:position] + character + string[(position+1):]
    # Returns the modified string
    return mutated_string

if __name__ == '__main__':
    # Grab the original string as the first input
    s = input()
    # Grab the index and the character that the index will be updated to
    i, c = input().split()
    # Call on the mutation function declared above
    s_new = mutate_string(s, int(i), c)
    # Output the modified string
    print(s_new)