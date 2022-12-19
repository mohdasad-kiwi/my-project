# Find all duplicate characters in string

def count(val):
    duplicate = []                         # Empty List
                                           # @param  str
    for char in val:

        if val.count(char) > 1 and char not in duplicate:
            duplicate.append(char)            # Checking the Duplicate

                     # Adding Duplicate to the empty list

    return duplicate                       # Returning list

val = input("Enter the string : ").strip()
print(count(val))
