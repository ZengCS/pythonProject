import matplotlib.pyplot as plt
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()

# Create the x and y arrays for the panda's eyes
x_eyes = [0.2, 0.8]
y_eyes = [0.8, 0.8]

# Plot the eyes as circles
ax.scatter(x_eyes, y_eyes, s=100, color='blue')

# Create the x and y arrays for the panda's body
t = np.linspace(0, 2 * np.pi, 100)
x_body = 0.5 + 0.3 * np.cos(t)
y_body = 0.5 + 0.3 * np.sin(t)

# Plot the body as a black and white filled circle
ax.fill(x_body, y_body, color='black', alpha=0.7)
ax.fill(x_body, y_body, color='white', alpha=0.3)

# Show the plot
plt.show()
