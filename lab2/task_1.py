import numpy as np
import matplotlib.pyplot as plt

random_numbers = np.random.normal(0, 1, 10000)

plt.hist(random_numbers, bins=25, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
