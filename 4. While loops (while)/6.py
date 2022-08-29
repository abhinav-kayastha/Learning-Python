import random

numbersOfPoints = int(input("Enter a large integer number: "))
pointsInsideCircle = 0

for x in range(numbersOfPoints):
    pointX = random.uniform(-1, 1)
    pointY = random.uniform(-1, 1)
    if pointX ** 2 + pointY ** 2 < 1:
        pointsInsideCircle = pointsInsideCircle + 1
    else:
        continue

piApproximation = (4 * pointsInsideCircle)/numbersOfPoints
print(f"Approximation of pi is {piApproximation}")
