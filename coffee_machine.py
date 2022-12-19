# Coffee Machine Prog

choice = int(input())
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]
try:

    if choice in range(len(coffee)):
        print(coffee[choice])


except:
    print("Invalid Choice")


finally:
    print("Have a good day")
