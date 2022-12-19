# program for odd Numbers

# taking Input from User

user_input = int(input("enter the range you want the Odd No :-"))

# Looping
for i in range(1, user_input+1):
    if i % 2 != 0:
        print(i, end=",")



