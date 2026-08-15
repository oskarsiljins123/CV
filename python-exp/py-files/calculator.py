def options():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
while True:
    first_num = input("Enter the first number: ")
    if first_num.isdigit():
        break
    else:
        print("Please enter a valid number.")
options()
while True:
    choice = input("Choose an option: ")
    if choice in ["1", "2", "3", "4"]:
        break
    else:
        print("Please choose a valid option.")
while True:
    second_num = input("Enter the second number: ")
    if second_num.isdigit():
        break
    else:
        print("Please enter a valid number.")
if choice == "1":
    print(int(first_num) + int(second_num))
elif choice == "2":
    print(int(first_num) - int(second_num))
elif choice == "3":
    print(int(first_num) * int(second_num))
elif choice == "4":
    print(int(first_num) / int(second_num))  
