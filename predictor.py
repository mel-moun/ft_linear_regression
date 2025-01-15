import pandas as pd
from calculations import ft_mean, ft_std


def main():
    try:
        df = pd.read_csv('data.csv')
        mileage = df['km']
        price = df['price']

        mean = ft_mean(mileage)
        std_var = ft_std(mileage)

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
        