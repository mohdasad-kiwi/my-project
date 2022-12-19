# convert Set into Tuple and Tuple into Set
# Input: {'a', 'b', 'c', 'd', 'e'}
# Output: ('a', 'c', 'b', 'e', 'd')


my_tuple = (input('Enter space-separated words: ').split())
print(my_tuple)
x = [element for element in my_tuple]
print(tuple(x))
