import matplotlib
import math

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

equation = lambda x, m, b: m * x + b

x = np.linspace(0, 100, 100)
m = 37/20.7364413533
b = 500

y = equation(x, m, b)

plt.plot(x, y)
plt.show()