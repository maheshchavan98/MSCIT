#pip install neurodynex

from neurodynex.hopfield_network import network, pattern_tools, plot_tools
import matplotlib.pyplot as plt
import numpy as np

pattern_size = 5
hopfield_net = network.HopfieldNetwork(nr_neurons=pattern_size**2)

# Create pattern factory for generating patterns
factory = pattern_tools.PatternFactory(pattern_size, pattern_size)

# Generate a checkerboard pattern
checkerboard = factory.create_checkerboard()

# Create a list of patterns including random patterns
pattern_list = [checkerboard]
pattern_list.extend(factory.create_random_pattern_list(nr_patterns=3, on_probability=0.5))

# Plot the patterns
plot_tools.plot_pattern_list(pattern_list)

# Compute and plot the overlap matrix
overlap_matrix = pattern_tools.compute_overlap_matrix(pattern_list)
plot_tools.plot_overlap_matrix(overlap_matrix)

# Flatten the patterns before storing them in the Hopfield network
pattern_list_flat = [pattern.flatten() for pattern in pattern_list]
hopfield_net.store_patterns(pattern_list_flat)

# Create a noisy initial state by flipping 4 bits in the checkerboard
noisy_init_state = pattern_tools.flip_n(checkerboard, nr_of_flips=4)

# Set the initial state in the Hopfield network
hopfield_net.set_state_from_pattern(noisy_init_state.flatten())  # Flatten initial state if necessary

# Run the network with monitoring for 4 steps
states = hopfield_net.run_with_monitoring(nr_steps=4)

# Reshape the states to match the pattern size
states_as_patterns = factory.reshape_patterns(states)

# Plot the state sequence and overlap with the reference pattern
plot_tools.plot_state_sequence_and_overlap(states_as_patterns, pattern_list, reference_idx=0, suptitle="Network dynamics")

#pip install neurodynex
