import random

numbersOfPoints = 1000000
pointsInsideCircle = 0

for x in range(numbersOfPoints):
    pointX = random.gauss(-1, 1)
    pointY = random.gauss(-1, 1)

    if pointX ** 2 + pointY ** 2 < 1:
        pointsInsideCircle = pointsInsideCircle + 1
    else:
        continue

print(pointsInsideCircle)
piApproximation = (4 * pointsInsideCircle)/numbersOfPoints
print(f"Approximation of pi is {piApproximation}")
