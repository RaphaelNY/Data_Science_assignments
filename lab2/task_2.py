import numpy as np
import matplotlib.pyplot as plt

pop = np.random.normal(1, 50, 2000)

means_size_100 = [np.mean(np.random.choice(pop, size=100)) for _ in range(10000)]

plt.hist(means_size_100, bins=30, color='g')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid()
plt.show()
