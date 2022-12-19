# Replace String by nth Dictionary value
# Input :
# test_list = [“ABC”, “is”, “Best”] subs_dict = {“ABC” : [5, 6, 7], “is” : [7, 4, 2]}
# K = 0
# Output : [5, 7, “Best”]

def sub_dict_comb(test_list):
    for i in range (len(test_list)):
        subs_dict[test_list[i]] = input(f"Enter list element as a value of the key {test_list[i]} seperated by space: ").strip().split(" ")

def replacing_function(test_list,subs_dict):
    k = int(input("Enter Kth index of value list you want to replace with: "))

    replaced_list = [element if element not in subs_dict else int(subs_dict[element][k]) for element in test_list]

    return replaced_list

test_list=input("Enter element of list seperated by space: ").strip().split(" ")
subs_dict = dict()
sub_dict_comb(test_list)
print(replacing_function(test_list, subs_dict))



