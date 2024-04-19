# Description: Given a string, split the string along a " "(space) delimeter
#  and join the list using a "-" hyphen.
# Sample Input : this is a string
# Sample Output : this-is-a-string

# Declare function used to split and join the string
def split_and_join(line):
    # Write your code here
    # Declare the list of strings that is created by the split operator
    split_line = line.split(" ")
    # Join the list of strings using a hyphen as a spacer
    hyphen_line = "-".join(split_line)
    # Return the joined string
    return hyphen_line

if __name__ == '__main__':
    # Take in the string from the input
    line = input()
    # Call the split and join function to get the hyphenated line
    result = split_and_join(line)
    # Output the results
    print(result)