import matplotlib.pyplot as mat
import numpy as np

Height = [1.70, 1.62, 1.52, 1.85, 1.91, 1.42]
Weight = [72, 64, 84, 80, 72, 70]

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
mat.scatter(Height, Weight)

# regression line
mat.plot(Height, predictedWeight)
mat.xlabel("Height")
mat.ylabel("Weight")
mat.title("Linear Regression")
mat.show()