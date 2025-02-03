from mvpa2 import *
from mvpa2.mappers.som import SimpleSOMMapper
import numpy as np
import matplotlib.pyplot as plt

# Define colors and color names
colors = np.array([[0., 0., 0.],
                   [0., 0., 1.],
                   [0., 0., 0.5],
                   [0.125, 0.529, 1.0],
                   [0.33, 0.4, 0.67],
                   [0.6, 0.5, 1.0],
                   [0., 1., 0.],
                   [1., 0., 0.],
                   [0., 1., 1.],
                   [1., 0., 1.],
                   [1., 1., 0.],
                   [1., 1., 1.],
                   [0.33, 0.33, 0.33],
                   [0.5, 0.5, 0.5],
                   [0.66, 0.66, 0.66]])

color_names = ['black', 'blue', 'darkblue', 'skyblue', 'greyblue', 'lilac', 
               'green', 'red', 'cyan', 'violet', 'yellow', 'white', 
               'darkgrey', 'mediumgrey', 'lightgrey']

# Create and train the SOM
som = SimpleSOMMapper((2., 30), 400, learning_rate=0.05)
som.train(colors)

# Plot the SOM weight map
plt.imshow(som.K, origin='lower')
plt.title('Colors SOM')

# Map the input colors to the SOM
mapped = som(colors)

# Plot color names at each mapped position
for i, m in enumerate(mapped):
    plt.text(m[1], m[0], color_names[i], ha='center', va='center',
             bbox=dict(facecolor='white', alpha=0.5, lw=0))

# Show the plot
plt.show()
