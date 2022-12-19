# Using the merge operator (|), we can combine dictionaries in a single line of code.

# Taking First Dict from user
fir = int(input("Enter the No of pair you want to create of keys and values in First Dict : "))
d1 = dict(input("Enter key and value saperated by space : ").split() for _ in range(fir))

# Taking Second Dict from user
sec = int(input("Enter the No of pair you want to create of keys and values in Second Dict : "))
d2 = dict(input("Enter key and value saperated by space : ").split() for _ in range(sec))
# using Merge Operator
# d3 = d2 | d1
# Output
#print(d3)
d1.update(d2)
print(d1)
