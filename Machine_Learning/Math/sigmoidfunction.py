import numpy as np
import matplotlib.pyplot as plt

# Generating x values from 1 to 999
x = np.arange(0,1,0.01)

# Computing log(1-x)
y = np.log(1 - x)

# Plotting
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('log(1-x)')
plt.title('Graph of log(1-x) for x from 1 to 999')
plt.grid(True)
plt.show()