gender = input("Enter your gender (M/F): ")

if gender == "F":
    hemoglobinValue = int(input("Enter your hemoglobin value (g/l): "))
    if 117 <= hemoglobinValue <= 155:
        print("Normal hemoglobin.")
    elif hemoglobinValue > 155:
        print("High hemoglobin.")
    elif hemoglobinValue < 117:
       print("Low hemoglobin")

elif gender == "M":
    hemoglobinValue = int(input("Enter your hemoglobin value (g/l): "))
    if 134 <= hemoglobinValue <= 167:
        print("Normal hemoglobin.")
    elif hemoglobinValue > 167:
        print("High hemoglobin.")
    elif hemoglobinValue < 134:
        print("Low hemoglobin.")

else:
    print("Enter a valid gender.")