# Description: Given three integer x, y and z representing dimensions
#  of a cuboid. Print the list of all possible cordinates (i, j, k) on
#  a 3D grid where the sum i + j + k is not equal to n.
# Sample input : 1, 1, 1, 2
# Sample output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
if __name__ == '__main__':
    # Take in the 4 integers used for the input
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # Declare the initial array for the output
    initial_list = []
    # Fill in each possible combination of coordinates
    for n1 in range(x+1):
        for n2 in range(y+1):
            for n3 in range(z+1):
                initial_list.append([n1, n2, n3])
    # Filter the list to only account for entries that meet the condition
    final_list = [entry for entry in initial_list if 
                  entry[0] + entry[1] + entry[2] != n]
    # Output the solution
    print(final_list)