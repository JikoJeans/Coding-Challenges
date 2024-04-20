# Description: In this challenge, the user enters a string and a substring.
# The output should be the number of times that the substring occurs in the
# given string. String traversal will take place from left to right, not
# from right to left.
# Sample Input : ABCDCDC
#                CDC
# Sample Output : 2

# Define the function used to count the number of substring occurances
def count_substring(string, sub_string):
    # Declare a count variable and set it to 0
    count = 0
    # For each potential substring we will check to see if it is a match
    for index in range(0, len(string) - len(sub_string) + 1):
        # Declare a temperary string that contains the sub string
        split_string = string[index : index + len(sub_string)]
        # Check for a match between the split string and the target sub string
        if sub_string in split_string:
            count = count + 1
    # Return the count found
    return count

if __name__ == '__main__':
    # Take in the initial string and trim any white space
    string = input().strip()
    # Take in the sub string that we want to match
    sub_string = input().strip()
    # Call the count function that returns the number of sub strings found in
    #  in the initial string as defined above
    count = count_substring(string, sub_string)
    # Output the total count found
    print(count)