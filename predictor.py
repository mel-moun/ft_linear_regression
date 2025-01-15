import pandas as pd
import matplotlib.pyplot as plt
from calculations import ft_mean, ft_std


def calculate_cost(theta0, theta1, mileage, price):
    m = len(mileage)
    predictions = theta1 * mileage + theta0
    cost = (1 / (2 * m)) * sum((predictions - price) ** 2)
    return cost


def gradient_descent(mileage, price):
    theta0 = 0
    theta1 = 0
    learning_rate = 0.01
    iterations = 1000

    m = len(mileage)
    cost_history = []

    for i in range(iterations):
        predictions = theta1 * mileage + theta0
        error = predictions - price
        gradient_theta0 = (1 / m) * sum(error)
        gradient_theta1 = (1 / m) * sum(error * mileage)
        theta0 -= learning_rate * gradient_theta0
        theta1 -= learning_rate * gradient_theta1
        cost = calculate_cost(theta0, theta1, mileage, price)
        cost_history.append(cost)

    print(f"theta0: {theta0}\ntheta1: {theta1}")

    return theta0, theta1, cost_history


def plot_single_graph(x, y, xlabel, ylabel, title, color='green', label=None):
    plt.plot(x, y, color=color, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if label:
        plt.legend()


def plot_graphs(mileage, price, cost_history, theta0, theta1):
    plt.figure(figsize=(14, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(mileage, price, label='Data points', color='blue')
    plot_single_graph(mileage,
                      theta1 * mileage + theta0,
                      'Mileage', 'Price', 'Data and hypothesise',
                      'green', 'Linear regression')

    plt.subplot(1, 2, 2)
    plot_single_graph(range(1000),
                      cost_history,
                      'Iterations',
                      'Loss',
                      'Loss over time',
                      'green')

    plt.tight_layout()
    plt.show()


def main():
    try:
        df = pd.read_csv('data.csv')
        mileage = df['km']
        price = df['price']

        mean = ft_mean(mileage)
        std_var = ft_std(mileage)
        normalize_mileage = (mileage - mean) / std_var

        theta0, theta1, cost_history = gradient_descent(normalize_mileage,
                                                        price)

        theta0 = theta0 - theta1 * (mean / std_var)
        theta1 = theta1 / std_var

        with open('thetas.txt', 'w') as file:
            file.write(f"{theta0},{theta1}")

        plot_graphs(mileage, price, cost_history, theta0, theta1)

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
