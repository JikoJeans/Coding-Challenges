# Description: Given an intger, n, and n space-seperated integers as an input,
#  create a tuple, t, of those n integers. Them compute and print the result
#  of hash(t).
# Sample Input : 2
#                1 2
# Sample Output : 3713081631934410656
if __name__ == '__main__':
    # Take in the number of integers
    n = int(input())
    # Take in each integer by splitting on spaces
    integer_list = map(int, input().split())
    # Declare the tuple with the integer list
    integer_tuple = tuple(integer_list)
    # Output the hash of the tuple
    print(hash(integer_tuple))