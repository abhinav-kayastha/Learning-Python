def convert_to_liters(gallons):
    liters = gallons * 3.785
    return liters

while True:
    volumeInGallons = float(input("Enter volume in gallons: "))
    if volumeInGallons < 0:
        break
    else:
        print("In liters: " +  str(convert_to_liters(volumeInGallons)))
        continue

