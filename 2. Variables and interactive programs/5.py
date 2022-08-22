talent = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

inGrams = (talent * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)

print("The weight in modern units: " + str(int(inGrams//1000)) + " kilograms" + " and " + str(inGrams % 1000) + " grams.")