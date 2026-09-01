import matplotlib.pyplot as mat
import numpy as np

Height = [
    1.70, 1.62, 1.52, 1.85, 1.91, 1.42,
    1.68, 1.75, 1.59, 1.82, 1.73, 1.66,
    1.78, 1.55, 1.88, 1.64, 1.71, 1.49,
    1.80, 1.57, 1.69, 1.76, 1.61, 1.84,
    1.53, 1.72, 1.67, 1.90, 1.58, 1.74
]

Weight = [
    72, 64, 84, 80, 72, 70,
    68, 76, 58, 82, 71, 65,
    79, 55, 85, 62, 74, 52,
    88, 60, 69, 77, 63, 81,
    57, 73, 67, 91, 59, 75
]

# slope
m = np.cov(Height, Weight)[0][1] / np.var(Height)

# intercept
c = np.mean(Weight) - m * np.mean(Height)

print("m =", m)
print("c =", c)

# predicted weight
predictedWeight = []

for x in Height:
    predictedWeight.append(m * x + c)

# scatter plot
mat.scatter(Height, Weight,color="red")

# regression line
mat.plot(Height, predictedWeight)
mat.xlabel("Height")
mat.ylabel("Weight")
mat.title("Linear Regression")
mat.show()