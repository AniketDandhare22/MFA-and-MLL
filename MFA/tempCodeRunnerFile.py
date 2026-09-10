import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("virus_bacteria_data.csv")
viral = data[data["Class"] == "Virus"]
bacteria = data[data["Class"] == "Bacteria"]

plt.scatter(viral["CRP"],viral["Temperature"] , color="green")
plt.scatter(bacteria["CRP"],bacteria["Temperature"] , color="orange")
plt.show()
