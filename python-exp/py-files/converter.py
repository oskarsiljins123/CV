def measurments():
    print("avaiable measurments:")
    print("KM")
    print("M")
    print("CM")
    print("MM")
measurments()
while True:
    measurment = input("Choose a measurment that you want to convert: ").upper()
    if measurment in ["KM", "M", "CM", "MM"]:
        break 
while True:
    amount = input("Enter the amount that you want to convert: ")
    if amount.isdigit():
        break
while True:
    convert_to = input("Choose a measurment that you want to convert to: ").upper()
    if convert_to in ["KM", "M", "CM", "MM"]:
        break
if measurment == "KM":
    if convert_to == "M":
        print(f"{amount} KM is equal to {int(amount) * 1000} M")
    elif convert_to == "CM":
        print(f"{amount} KM is equal to {int(amount) * 100000} CM")
    elif convert_to == "MM":
        print(f"{amount} KM is equal to {int(amount) * 1000000} MM")
if measurment == "M":
    if convert_to == "KM":
        print(f"{amount} M is equal to {int(amount) / 1000} KM")
    elif convert_to == "CM":
        print(f"{amount} M is equal to {int(amount) * 100} CM")
    elif convert_to == "MM":
        print(f"{amount} M is equal to {int(amount) * 1000} MM")
if measurment == "CM":
    if convert_to == "KM":
        print(f"{amount} CM is equal to {int(amount) / 100000} KM")
    elif convert_to == "M":
        print(f"{amount} CM is equal to {int(amount) / 100} M")
    elif convert_to == "MM":
        print(f"{amount} CM is equal to {int(amount) * 10} MM")
if measurment == "MM":
    if convert_to == "KM":
        print(f"{amount} MM is equal to {int(amount) / 1000000} KM")
    elif convert_to == "M":
        print(f"{amount} MM is equal to {int(amount) / 1000} M")
    elif convert_to == "CM":
        print(f"{amount} MM is equal to {int(amount) / 10} CM")