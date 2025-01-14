def read_thetas():
    with open("thetas.txt", "r") as data:
        thetas = data.read().strip().split(',')
        thetas[0] = float(thetas[0])
        thetas[1] = float(thetas[1])
    return thetas

def main():
    try:
        mileage = float(input("Enter a mileage: "))

        read_thetas()
    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
