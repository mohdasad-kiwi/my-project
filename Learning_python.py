# List Comprihensions
ls=[i for i in range(100) if i%3==0]
print(ls)

# Dict Comprihensions
dic= {i:f"item {i}" for i in range(1001) if i%100==0}
print(dic)

# Reversed dict
dic2 = {value:key for key,value in dic.items() }
print(dic2)

# Taking List as input from User
size_test_list = int(input("Enter the size of the list "))
size_list = list(num for num in input("Enter the list items separated by space ").strip().split())[:size_test_list]
print("test list = ", size_list)

# Taking Dict as input from user
size_subs_dict = int(input("Enter the No of pair you want to create of keys and values in Dict : "))
subs_dict = {}
for i in range(size_subs_dict):
    key =input("Enter the key Value ")
    value = list(val for val in input("Enter the value of your given key in form of list items separated by space ").strip().split())[:3]
    subs_dict[key]=value
print(dict)
