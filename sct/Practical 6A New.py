import numpy as np
from minisom import MiniSom
import matplotlib.pyplot as plt


colors = np.array([
    [0., 0., 0.],    
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
    [0.66, 0.66, 0.66]   
])

color_names = [
    'black', 'blue', 'darkblue', 'skyblue', 'greyblue', 'lilac', 
    'green', 'red', 'cyan', 'violet', 'yellow', 'white', 
    'darkgrey', 'mediumgrey', 'lightgrey'
]

som = MiniSom(x=10, y=10, input_len=3, sigma=1.0, learning_rate=0.5)
som.train_batch(colors, 1000)  
plt.figure(figsize=(12, 10))
plt.imshow(som.distance_map().T, cmap='bone', origin='lower')
for i, color in enumerate(colors):
    w = som.winner(color)
    plt.text(w[1], w[0], color_names[i], ha='center', va='center',
             bbox=dict(facecolor='white', alpha=0.5, lw=0))
som_weights = som.get_weights()
n_rows, n_cols = som_weights.shape[0], som_weights.shape[1]
for i in range(n_rows):
    for j in range(n_cols):
        plt.plot(j, i, 'ko')  

plt.title('SOM Grid and Distance Map')
plt.show()
#pip install minisom