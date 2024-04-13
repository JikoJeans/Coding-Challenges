# Description: Given three integer x, y and z representing dimensions
#  of a cuboid. Print the list of all possible cordinates (i, j, k) on
#  a 3D grid where the sum i + j + k is not equal to n.
# Sample input : 1, 1, 1, 2
# Sample output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    initial_list = []
    for n1 in range(x+1):
        for n2 in range(y+1):
            for n3 in range(z+1):
                initial_list.append([n1, n2, n3])
    
    final_list = [entry for entry in initial_list if 
                  entry[0] + entry[1] + entry[2] != n]
    print(final_list)   