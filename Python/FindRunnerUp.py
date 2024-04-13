# Description: Given a score sheet you are tasked with determining the
#  runner-up score. The runner-up in the list should be the second
#  largest number found like in the example below.
# Sample input : 5
#                2 3 6 6 5
# Sample output: 5
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    curr_max = -100
    curr_runner = -100
    for index in arr:
        if curr_max < index:
            curr_runner = curr_max
            curr_max = index
        elif curr_runner < index and curr_max > index:
            curr_runner = index
            
    print(curr_runner)