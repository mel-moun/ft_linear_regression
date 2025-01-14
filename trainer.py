def read_thetas():
    try:
        with open("thetas.txt", "r") as data:
            thetas = data.read().strip().split(',')
            thetas = [float(x) for x in thetas]
        return thetas
    except BaseException:
        return [0, 0]


def estimate_price(mileage, thetas):
    return thetas[0] + (thetas[1] * mileage)


def main():
    try:
        mileage = float(input("Enter a mileage: "))
        thetas = read_thetas()
        print("Estimated price:", estimate_price(mileage, thetas))
    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
