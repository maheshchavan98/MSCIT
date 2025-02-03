from __future__ import print_function
from __future__ import division
import numpy as np

class ART:
    def __init__(self, n=5, m=10, rho=.5):
        self.F1 = np.ones(n)          # Initial input field
        self.F2 = np.ones(m)          # Initial output field
        self.Wf = np.random.random((m, n))  # Forward weights
        self.Wb = np.random.random((n, m))  # Backward weights
        self.rho = rho                # Vigilance parameter
        self.active = 0               # Active neuron index

    def learn(self, X):
        self.F2[...] = np.dot(self.Wf, X)
        I = np.argsort(self.F2[:self.active].ravel())[::-1]
        for i in I:
            d = (self.Wb[:,i] * X).sum() / X.sum()  # Similarity measure
            if d >= self.rho:  # Match condition
                self.Wb[:, i] *= X   # Update weights
                self.Wf[i, :] = self.Wb[:, i] / (0.5 + self.Wb[:, i].sum())
                return self.Wb[:, i], i
        if self.active < self.F2.size:  # If no match, create a new active neuron
            i = self.active
            self.Wb[:, i] *= X
            self.Wf[i, :] = self.Wb[:, i] / (0.5 + self.Wb[:, i].sum())
            self.active += 1
            return self.Wb[:, i], i
        return None, None   # If no suitable neuron is found, return None


if __name__ == '__main__':
    np.random.seed(1)  # For reproducibility
    network = ART(5, 10, rho=0.5) # Create ART network instance
    data = [
        " O ", " O O", " O", " O O", " O", " O O", " O", " OO O", " OO ", 
        " OO O", " OO ", "OOO ", "OO ", "O ", "OO ", "OOO ", "OOOO ", 
        "OOOOO", "O ", " O ", " O ", " O ", " O", " O O", " OO O", " OO ",
        "OOO ", "OO ", "OOOO ", "OOOOO"
    ]    # Define the dataset (list of strings)

    max_length = max(len(s) for s in data)
    for i in range(len(data)):
        X = np.zeros(max_length)
        for j in range(len(data[i])):
            if data[i][j] == 'O':
                X[j] = 1
        Z, k = network.learn(X)
        if k is not None:
            print("|%s| -> class %d" % (data[i], k))
        else:
            print("|%s| -> no class assigned" % data[i])
