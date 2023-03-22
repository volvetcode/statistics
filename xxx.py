# Import Library

import matplotlib.pyplot as plt

# Define Data

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot

plt.plot(x, y, color='green', linewidth=3, linestyle='dotted')

# Display

plt.show(block=False)

# Print Statement

print('My First Matplotlib Program')

# Hold the plot

plt.pause(1000)