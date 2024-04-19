# Description: Given a string, swap the lower case letters to upper case and
#  swap the upper case letters to lower case.
# Sample Input : HackerRank.com presents "Pythonist 2".
# Sample Output : hACKERrANK.COM PRESENTS "pYTHONIST 2".

# Function used to perform the swap case
def swap_case(s):
    # Declare the string that will store the inverted case
    s_inverted = ""
    # Check each character in the origical string and invert the case if applicable
    for char in s:
        # Check for upper case and invert to lower
        if char.isupper():
            s_inverted += char.lower()
        # Check for lower case and invert to upper
        elif char.islower():
            s_inverted += char.upper()
        # Any other character can be left as is like numbers
        else:
            s_inverted += char
    # Return the inverted string
    return s_inverted

if __name__ == '__main__':
    # Grab the input string
    s = input()
    # Perform the swap case function with the input
    result = swap_case(s)
    # Output the string that has a case swapped.
    print(result)