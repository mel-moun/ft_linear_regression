import pandas as pd


def calculate_r2(mileage, price, theta0, theta1):
    """Calculates the R-squared value for a linear regression model.
        R-squared, or the coefficient of determination,
        measures how well a regression model explains the variability
        of the dependent variable.
        It ranges from 0 to 1, where:

    - 0 indicates that the model explains none of the variability.
    - 1 indicates that the model explains all the variability."""

    predictions = theta1 * mileage + theta0
    rss = sum((price - predictions) ** 2)
    tss = sum((price - price.mean()) ** 2)
    r_squared = 1 - (rss / tss)
    return r_squared


def main():
    """Reads input data
    and calculates the R-squared value for the dataset."""
    try:
        with open("thetas.txt", "r") as data:
            thetas = data.read().strip().split(',')
            thetas = [float(x) for x in thetas]

        df = pd.read_csv('data.csv')
        mileage = df['km']
        price = df['price']

        r_squared = calculate_r2(mileage, price, thetas[0], thetas[1])
        print(f"R-squared: {r_squared}")

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
