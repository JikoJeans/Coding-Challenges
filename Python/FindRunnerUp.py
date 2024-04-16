# Description: Given a score sheet you are tasked with determining the
#  runner-up score. The runner-up in the list should be the second
#  largest number found like in the example below.
# Sample input : 5
#                2 3 6 6 5
# Sample output: 5
if __name__ == '__main__':
    # Take in the input values for the scenerio
    n = int(input())
    arr = map(int, input().split())
    # Declare the minimum score as the maximum
    curr_max = -100
    curr_runner = -100
    # Find the second highest score in the array
    for index in arr:
        # If we find a new high score then update both the runner and max
        if curr_max < index:
            curr_runner = curr_max
            curr_max = index
        # If we find a new second highest score then update the runner appropriately
        elif curr_runner < index and curr_max > index:
            curr_runner = index
    # Output the results
    print(curr_runner)