import pandas as pd


def calculate_r2(mileage, price, theta0, theta1):
    predictions = theta1 * mileage + theta0
    residual_sum_of_squares = sum((price - predictions) ** 2)
    total_sum_of_squares = sum((price - price.mean()) ** 2)
    r_squared = 1 - (residual_sum_of_squares / total_sum_of_squares)
    return r_squared


def main():
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
