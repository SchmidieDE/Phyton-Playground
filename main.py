import numpy as np
import mutplotlib.pyplot as plt

pizzaPrices = np.array([24, 25, 28, 30, 40, 36, 32], [5.5, 8.9, 7.4, 10.9, 19.4, 13.8, 14])

x = pizzaPrices[0, :]
y = pizzaPrices[1, :]

plt.scatter(x, y, c='r')
