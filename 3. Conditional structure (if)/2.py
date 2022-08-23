cabinClass = input("Enter the cabin class: ")

if cabinClass == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabinClass == "A":
    print("A: above the car deck, equipped with a window.")
elif cabinClass == "B":
    print("B: windowless cabin above the car deck.")
    print("B: windowless cabin below the car deck.")
else:
    print("Enter a valid cabin class.")