# Description: You are given a first name and a last name of a person on two
#  different lines. Output the following with the name:
#   Hello firstname lastname! You just delved into python.
# Sample Input : Ross
#                Taylor
# Sample Output : Hello Ross Taylor! You just delved into python.

# Declare function used for printing out the output
def print_full_name(first, last):
    # Write your code here
    # Using f strings we can format the output as follows
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    # Take in the first name
    first_name = input()
    # Take in the last name
    last_name = input()
    # Output both names using the function above
    print_full_name(first_name, last_name)