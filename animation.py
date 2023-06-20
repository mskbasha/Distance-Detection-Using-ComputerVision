import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate some random points
x = np.random.rand(50)
y = np.random.rand(50)

fig, ax = plt.subplots()
scatter = ax.scatter(x, y)


def update(frame):
    # Generate new random points
    x = np.random.rand(50)
    y = np.random.rand(50)
    scatter.set_offsets(np.c_[x, y])
    return scatter,


ani = FuncAnimation(fig, update, frames=range(50), interval=200)
plt.show()
