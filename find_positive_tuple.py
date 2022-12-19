# Python program to find Tuples with positive elements in List of tuples
# Input :
# [(56, 43), (-31, 21, 23), (51, -65, 26), (24, 56)]
# OUTPUT:
# [(56, 43), (24, 56)]

# Checking each element of tuple of list for positive tuples
def sorting_tup(ele):
    # @ param ele tuple
    # return Boolean
    if all(element >= 0 for element in ele):
        return True
    else:
        return False

# Asking number of tuples user want to append in list
list_size = int(input("Enter no. of tuples you want to append in list: "))
list_of_tup = list()

# Taking user input for adding tup in a list
for i in range(0, list_size):
    user_input = input(f'Enter element of tuple {i+1} space-separated integers: ')
    tuple_ele = tuple(int(item) for item in user_input.split())
    list_of_tup.append(tuple_ele)

# Applying filter method to filter positive tuples
sorted_list = list(filter(sorting_tup, list_of_tup))

# Printing sorted list
print(sorted_list)
