def read_thetas():
    """
        Reads the theta values (model parameters)
        from the file 'thetas.txt'.

        If the file cannot be read,
        it returns default values [0, 0].
    """

    try:
        with open("thetas.txt", "r") as data:
            thetas = data.read().strip().split(',')
            thetas = [float(x) for x in thetas]
        return thetas
    except BaseException:
        return [0, 0]


def estimate_price(mileage, theta1, theta2):
    """
        Estimates the price based on the mileage and model parameters.
        The formula used is:
            price = theta1 + (theta2 * mileage)
    """

    return theta1 + (theta2 * mileage)


def main():
    """
        Prompts the user to input a mileage,
        reads model parameters,
        estimates the price using the regression model,
        and prints the result.
    """

    try:
        mileage = float(input("Enter a mileage: "))
        thetas = read_thetas()
        print(estimate_price(mileage, thetas[0], thetas[1]))
    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
