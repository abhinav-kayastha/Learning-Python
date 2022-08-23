zanderLength = int(input("Enter the length of zander (cm): "))

if zanderLength < 42:
    print("Release the zander.")
    difference = str(42 - zanderLength)
    print(f"The zander is {difference} cm shorter than the size limit.")
else:
    print("Keep the zander.")