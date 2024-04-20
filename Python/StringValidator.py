# Description: In this challenge we are given a string as the input and must output
#  if the conditions are met for each case. Below are the 5 cases where the string has
#  unique functions to check if the conditions are met which consists of isalnum(),
#  isalpha(), isdigit(), islower(), isupper().
# Sample Input : qA2
# Sample Output : True
#                 True
#                 True
#                 True
#                 True

if __name__ == '__main__':
    s = input()
    # First declare the boolean used to track the true or false response 
    char_found = False
    # In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    # If char found becomes true then we can bypass checking sub strings and output true
    char_found = s.isalnum()
    if char_found is False:
        # Check each character to check if the string has any alphanumeric characters
        for char in s:
            # Once one is found break out of the loop and output the results
            if char.isalnum():
                char_found = True
                break
    print(char_found)

    # In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    # Reset char found variable
    char_found = False
    # If char found becomes true then we can bypass checking sub strings and output true
    char_found = s.isalpha()
    if char_found is False:
        # Check each character to check if the string has any alphabetical characters
        for char in s:
            # Once one is found break out of the loop and output the results
            if char.isalpha():
                char_found = True
                break
    print(char_found)
    
    # In the third line, print True if  has any digits. Otherwise, print False.
    # Reset char found variable
    char_found = False
    # If char found becomes true then we can bypass checking sub strings and output true
    char_found = s.isdigit()
    if char_found is False:
        # Check each character to check if the string has any digits
        for char in s:
            # Once one is found break out of the loop and output the results
            if char.isdigit():
                char_found = True
                break
    print(char_found)
    
    # In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    # Reset char found variable
    char_found = False
    # If char found becomes true then we can bypass checking sub strings and output true
    char_found = s.islower()
    if char_found is False:
        # Check each character to check if the string has any lowercase characters
        for char in s:
            # Once one is found break out of the loop and output the results
            if char.islower():
                char_found = True
                break
    print(char_found)
    
    # In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    # Reset char found variable
    char_found = False
    # If char found becomes true then we can bypass checking sub strings and output true
    char_found = s.isupper()
    if char_found is False:
        # Check each character to check if the string has any uppercase characters
        for char in s:
            # Once one is found break out of the loop and output the results
            if char.isupper():
                char_found = True
                break
    print(char_found)