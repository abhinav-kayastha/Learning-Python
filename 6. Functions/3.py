def gallonsToLiters(userVolume):
    return userVolume / 3.785


def main(userVolume):
    print(gallonsToLiters(userVolume))

main(userVolume = float(input("Enter your volume of gasoline in gallons: ")))