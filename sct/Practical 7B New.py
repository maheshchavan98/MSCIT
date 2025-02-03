import numpy as np

class HopfieldNetwork:
    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
        self.weights = np.zeros((n_neurons, n_neurons))

    def train(self, patterns):
        for pattern in patterns:
            pattern = pattern.reshape(-1, 1)
            self.weights += pattern @ pattern.T
        np.fill_diagonal(self.weights, 0)
        self.weights /= len(patterns)

    def predict(self, pattern, steps=10):
        for _ in range(steps):
            pattern = np.sign(self.weights @ pattern)
        return pattern

    def add_noise(self, pattern, noise_level=0.1):
        noisy_pattern = pattern.copy()
        n_noise = int(noise_level * len(pattern))
        noise_indices = np.random.choice(len(pattern), n_noise, replace=False)
        noisy_pattern[noise_indices] = -noisy_pattern[noise_indices]
        return noisy_pattern

if __name__ == "__main__":
    # Define binary patterns (example: two patterns of length 4)
    patterns = np.array([[1, -1, 1, -1],
                         [-1, 1, -1, 1]])

    # Initialize Hopfield network with 4 neurons
    hopfield_net = HopfieldNetwork(n_neurons=patterns.shape[1])

    # Train the network with the patterns
    hopfield_net.train(patterns)

    # Define a test pattern (example: the first pattern with noise)
    test_pattern = hopfield_net.add_noise(patterns[0], noise_level=0.5)

    # Predict the associated memory
    result = hopfield_net.predict(test_pattern)

    print("Test Pattern: ", test_pattern)
    print("Predicted Pattern: ", result)
