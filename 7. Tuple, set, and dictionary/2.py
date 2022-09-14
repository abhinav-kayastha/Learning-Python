nameList = []

while True:
    userName = input("Enter a name (empty string to quit): ")
    if userName == "":
        break
    elif userName in nameList:
        print("Existing name.")
    else:
        print("New name.")
        nameList.append(userName)

for name in nameList:
    print(name)

