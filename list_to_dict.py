# Accept list from the user and return the output as a dict containing
# odd position as key and the even position as value.

def listdic(key):               # Function
    if (key%2!=0):              # Checking is the given No is even or Not
        print("Please Enter the length of list of Even items to make Pairs")

    else:
        list = []               # Empty List
        for i in range(0, key):
            element = int(input(f"Enter the {i+1} Element :- "))    # Taking the Elements from user
            list.append(element)                         # Adding  Elements to List

        dic = {}                                         # Empty Dictonery
        for j in range(0, key, 2):
            dic.update({list[j]:list[j+1]})              # Updating Dictonery
        return "Dictonery = ", dic                        # Returning Output

key = int(input("Enter the length of list you want to create :- "))  # Length of List
print(listdic(key))                                      # Output