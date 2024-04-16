# Description: The provided code stub will read in a dictionary containing key/value
#  pairs consistent of a name and  list of marks for a list of students. Print the
#  average marks array for each student name provided and rounded to the 2nd decimal
#  place.
# Sample Input : {alpha: [20, 30, 40]}
#                {beta: [30, 50, 70]}
#                query_name = 'beta'
# Sample Output : 50.0
if __name__ == '__main__':
    # Take in the number of students present
    n = int(input())
    # Declare the marks dictionary
    student_marks = {}
    # Take in each student name and scores appropriately
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    # Take in the target name
    query_name = input()
    # Declare the count and total used for the average calculation
    total = 0
    count = 0
    # Perform the average calculation on the query name
    for score in student_marks[query_name]:
        count = count + 1
        total = total + score
    # Calculate the true average
    average = total/count
    # Formate the final value such that it has 2 decimal points
    print(format(average, '.2f'))