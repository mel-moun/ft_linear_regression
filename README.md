# 🚗 **ft_linear_regression**

## 📊 **Project Overview**

The aim of this project is to introduce you to the basic concept behind machine learning. In this project, you will create a program that predicts the price of a car using a **linear regression** model. This model is trained using a **gradient descent** algorithm, which helps the program learn the best relationship between the car's features (like mileage) and its price.

---

## 🧑‍🏫 **What is Linear Regression?**

Linear regression is a method that predicts the value of one thing (like a car's price) based on the value of another thing (like the car's mileage). It draws a straight line that best fits the data, and this line is used to make predictions.

In simple linear regression, we have:
- **One input (independent variable)**: For example, the car's mileage.
- **One output (dependent variable)**: For example, the car's price.

---

## 🔑 **Key Concepts**

### 1. **Linear Regression Model** ✍️

The model uses a simple mathematical equation to predict the car's price:

$$
y = \theta_0 + \theta_1 \cdot x
$$

Where:
- θ0: The value of y when x = 0; the starting point of the line on the y-axis.
- θ1: The rate at which y changes with a one-unit increase in x; the steepness of the line.

The goal is to adjust the values of θ0 and θ1 so the model's predictions are as close as possible to the actual car prices.

---

### 2. **Gradient Descent: How the Model Learns** 🏃‍♂️

**Gradient Descent** is a way for the model to learn the best values for θ0 and θ1. Imagine standing on a hill and wanting to find the lowest point. You take steps downhill. Gradient descent works the same way: it adjusts the values of θ0 and θ1 step-by-step to reduce the error in predictions, moving towards the best-fit line.

- It starts with random values for θ0 and θ1.
- Then, it gradually adjusts them by calculating the error (the difference between the predicted and actual prices).
- The model repeats this process until it finds the values that make the error as small as possible.

---

### 3. **Mean Squared Error (MSE)** 📉

**Mean Squared Error (MSE)** is a way to measure how well the model is predicting the car's price. It calculates the average of the squared differences between the actual prices and the predicted prices. The smaller the MSE, the better the model’s predictions are.

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

Where:
- ŷi : the predicted price.
- yi : the actual price.
- n : the number of data points.

---

### 4. **R-squared: How Good is the Model?** 📈

**R-squared (R²)** is a measure of how well the model explains the variation in the data. It tells us what percentage of the variation in car prices can be explained by the model. The value ranges from 0 to 1:
- **0** means the model explains none of the variation.
- **1** means the model perfectly explains the variation.

Mathematically, it’s calculated as:

$$
R^2 = 1 - \frac{\text{RSS}}{\text{TSS}}
$$

Where:
- **RSS (Residual Sum of Squares)** measures how much the predicted values differ from the actual values.
- **TSS (Total Sum of Squares)** measures how much the actual values differ from the mean.

The closer R-squared is to 1, the better the model is at predicting the price.

$$
\text{RSS} = \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

$$
\text{TSS} = \sum_{i=1}^n (y_i - \bar{y})^2
$$

Where:

- ȳ : is the mean (average) of all the observed values.

---

### 5. **Feature Scaling: Why We Do It** 🧮

Sometimes, the features used in a model have very different scales. For example, one feature might be the **car's mileage** in thousands of miles, while another could be the **price** in tens of thousands of dollars. If we don't scale the features, the model might give more importance to the feature with larger values.

**Feature scaling** helps by adjusting the values of the features so they are on a similar scale. We use **standardization**, which scales the features by removing the mean and dividing by the standard deviation:

$$
x_{\text{standardized}} = \frac{x - \mu}{\sigma}
$$

Where:
- x is the original value of a feature.
- μ is the mean (average) of the feature values.
- σ is the standard deviation of the feature values.

Standardizing the features helps the model learn more efficiently and avoid errors that might happen when one feature is much larger than the others.

---
