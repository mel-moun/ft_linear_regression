import pandas as pd
import matplotlib.pyplot as plt
from calculations import ft_mean, ft_std
from predictor import estimate_price


def calculate_cost(error):
    """
        Calculates the cost function (Mean Squared Error)
        for a linear regression model.

        The cost function evaluates how well the model's
        predictions match the actual data.

        Lower cost values indicate a better fit of the model to the data.
    """

    m = len(error)
    cost = (1 / (2 * m)) * sum(error ** 2)
    return cost


def gradient_descent(mileage, price):
    """"
        Performs gradient descent to find optimal
        linear regression parameters.

        Gradient descent is an optimization algorithm
        used to minimize the cost function.
        It iteratively updates the parameters (theta0 and theta1)
        to reduce the cost by calculating the gradients
        of the cost function with respect to these parameters.
    """

    theta0 = 0
    theta1 = 0
    learning_rate = 0.01
    iterations = 1000

    m = len(mileage)
    cost_history = []

    for _ in range(iterations):
        predictions = estimate_price(mileage, theta0, theta1)
        error = predictions - price

        cost = calculate_cost(error)
        cost_history.append(cost)

        tmp_theta0 = (1 / m) * sum(error)
        tmp_theta1 = (1 / m) * sum(error * mileage)

        theta0 -= learning_rate * tmp_theta0
        theta1 -= learning_rate * tmp_theta1

    print(f"theta0: {theta0}\ntheta1: {theta1}")

    return theta0, theta1, cost_history


def plot_single_graph(x, y, xlabel, ylabel, title, color='green', label=None):
    """
        Plots a single graph with the given data and labels.
    """

    plt.plot(x, y, color=color, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if label:
        plt.legend()


def plot_graphs(mileage, price, cost_history, theta0, theta1):
    """
        Plots the regression results and loss over time.
    """

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
    """
        Loads the data, normalizes it, performs regression,
        and visualizes results.
    """

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
