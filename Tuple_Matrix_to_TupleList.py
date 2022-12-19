# Convert Tuple Matrix to Tuple List
# Input : test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)]]
# Output : [(4, 7, 10, 18), (5, 8, 13, 17)]

test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]

print("The original list is : " + str(test_list))

# flattening
temp = [ele for sub in test_list for ele in sub]

# joining to form column pairs
res = list(zip(*temp))

# printing result
print("The converted tuple list : " + str(res))