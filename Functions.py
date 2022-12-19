# LIST FUNCTIONS
# append Function

list = []
list.append("Asad")
list.append("Ruman")
list.append("Grape")
print(list)

# Insert Function

list.insert(1, "apple")
list.insert(2, "Banana")
print(list)

# Remove Function

list.remove("Grape")
print(list)

# Extend Function

list2=["new","hub"]
list.extend(list2)
print(list)

# PoP Function

list.pop()
print(list)

# Sort Function

list.sort()
print(list)

# Reverse Function

list.reverse()
print(list)

# Count Function

print(list.count("Asad"))

# Index Function

print(list.index("Ruman"))

# TUPLE FUNCTIONS

tab=('new', 'apple', 'Ruman', 'Banana', 'Asad')

# Count Function

print(tab.count('new'))

# index Function

print(tab.index('Banana'))

# DICTONERY FUNCTIONS

dic={"python":1,"java":2,"c#":3}
dic2={"c++":4,"Html":5,"CSS":6}

# Copy Function

d2=dic.copy()
print(d2)

# Update function

(dic.update({"java":"clone"}))
print(dic)

# Value Function

print(dic.values())

# Keys Function

print(dic.keys())

# Items Function

print(dic.items())