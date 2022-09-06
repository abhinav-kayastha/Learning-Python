def pizza_unit_price_calc(diameter, price):
    radius = (diameter / 2) / 100
    area = 3.141592 * radius ** 2
    unit_price = price / area
    return unit_price


pizza_one_diameter = float(input("Enter the diameter of your first pizza (in cm): "))
pizza_one_price = float(input("Enter the price of your first pizza (in euros): "))
pizza_one_unit_price = pizza_unit_price_calc(pizza_one_diameter, pizza_one_price)

pizza_two_diameter = float(input("Enter the diameter of your second pizza (in cm): "))
pizza_two_price = float(input("Enter the price of your second pizza (in euros): "))
pizza_two_unit_price = pizza_unit_price_calc(pizza_two_diameter, pizza_two_price)

if pizza_one_unit_price < pizza_two_unit_price:
    print("Get the first pizza.")
else:
    print("Get the second pizza.")
