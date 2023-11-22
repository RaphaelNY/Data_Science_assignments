import numpy as np
from sklearn.utils import resample

list_boy = [1] * 1000
list_gil = [0] * 800
list_all = np.hstack((list_boy, list_gil))

times = 10000
n = 0

for i in range(times):
    bootstrapSamples = resample(list_all, n_samples=100, replace=1)
    n += np.sum(bootstrapSamples == 1)/100

average = n / times * 100

print("calculate average is ", average, "%")
print("raw data average is ", 1000/1800*100, "%")
