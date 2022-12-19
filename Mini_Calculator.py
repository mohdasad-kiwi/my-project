# Mini calculator

num1 = int(input("Enter 1st Number : "))    # First Number
num2 = int(input("Enter 2nd Number : "))    # Second Number
operator = input("So what do you want to do with the given numbers?'+','-','*','/'")    # Operation

if operator == '+':
    plus = num1+num2
    print("result =", plus)

elif operator == '-':
    minus = num1-num2
    print("result =", minus)

elif operator == '*':
    mul = num1*num2
    print("result =", mul)

elif operator == '/':
    dev = num1/num2
    print("result =", dev)

else:
    print("try another Number")
