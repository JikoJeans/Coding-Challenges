# Description: Given the name and grades for each student in class of N students,
#  store them as a nested list and print the name(s) of any student(s) having
#  the second lowest grade. Note: if there are multiple students tied for the
#  second lowest score then print each name on a new line.
# Sample Input : 5, Harry, 37.21, Berry, 37.21, Tina, 37.2, Akriti, 41, Harsh, 39
# Sample Output : Berry
#                 Harry
if __name__ == '__main__':
    # Declare the nested list that will be used to store the name and score
    records = []
    # Declare the two variables used to track the second lowest score and set them
    #  to the highest score possible
    lowest_score = 100
    second_lowest = lowest_score
    # Take in each input and store them into temperary variables
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # Add each entry into the full list of records
        records.append([name, score])
        # Track the second lowest score by utilizing two variables
        if(score < lowest_score):
            # If the score is the new lowest then update both values
            second_lowest = lowest_score
            lowest_score = score
        elif (score < second_lowest and score > lowest_score):
            # If the score greater than the lowest but less than the second lowest
            #  then update the second lowest variable
            second_lowest = score
    # Declare the name list used to alphabetize the names
    final_name_list = []
    for index in records:
        # Capture the name of the students with the second lowest score
        if index[1] == second_lowest:
            final_name_list.append(index[0])
    # Sort the list alphabetically
    final_name_list.sort()
    # Print out each name on a seperate line
    for index in final_name_list:
        print(index)