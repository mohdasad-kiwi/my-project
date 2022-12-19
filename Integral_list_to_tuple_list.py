# Convert Integral list to tuple list
#
# Input: [1, 4, 6, 8, 9]
# Output: [(1, ), (4, ), (6, ), (8, ), (9, )]

list = input("Enter the list Elements Seperated by the space between them :-")
list_elements = list.split(" ")

# printing original list
print("The original list : " + str(list_elements))

# Convert Integral list to tuple list
# using list comprehension
result = [(ele, ) for ele in test_list]

# printing result
print("List after conversion to tuple list : " + str(result))