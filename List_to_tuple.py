# Converting element of list into tuple

def ele_to_tup(ele):
# @ param ele str
# retrun tuple
    return tuple(list(ele))

# converting tuple of list into string

def tup_to_string(ele):
# @ param ele tuple
# return string
    return "".join(list(ele))

# Taking input from user
user_input = input("Enter element to convert them into tuple and store it in to list: ").strip().split(" ")
print(ele_to_tup(user_input))
print(tup_to_string(user_input))
