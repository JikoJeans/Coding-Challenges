# Description: Initialize a list and read in n followed by n lines of commands
#  where each command will be the 7 types listed below. Iterate through each command
#  in order and perform the corresponding operation on the list.
# Possible functions: insert(index, value), print(), remove(value), append(value),
#  sort(), pop(), and reverse().
# Sample Input : 12, insert 0 5, insert 1 10, insert 0 6, print, remove 6, append 9,
#  append 1, sort, print, pop, reverse, print
# Sample Output : [6, 5, 10]
#                 [1, 5, 9, 10]
#                 [9, 5, 1]
if __name__ == '__main__':
    # Take in the number of instructions given
    N = int(input())
    # Declare a list that will be used to emulate the input
    emulated_list = []
    # For each instruction given perform the operation
    for instruction_index in range(N):
        # The full instruction is passed including any values
        full_instruction = input()
        # Split the input to seperate out any values appended
        split_instruction = full_instruction.split(' ')
        # Take in the instruction type from the first index
        instruction_type = split_instruction[0]
        if instruction_type == 'insert':
            # Take in the operation using the format below
            # insert index value
            index = int(split_instruction[1])
            value = int(split_instruction[2])
            # Insert the value into the emulated list
            emulated_list.insert(index, value)
        elif instruction_type == 'print':
            # Print the emulated list
            print(emulated_list)
        elif instruction_type == 'remove':
            # Remove the value passed in by the operation with the format below
            # Remove value
            value = int(split_instruction[1])
            # Perform removal on emulated list
            emulated_list.remove(value)
        elif instruction_type == 'append':
            # Append a value passed in to the list with the format
            # append value
            value = int(split_instruction[1])
            # Perform append on emulated list
            emulated_list.append(value)
        elif instruction_type == 'sort':
            # Perform sort on emulated list
            emulated_list.sort()
        elif instruction_type == 'pop':
            # Perform pop on emulated list
            emulated_list.pop()
        else:
            # Perform reverse on emulated list
            emulated_list.reverse()