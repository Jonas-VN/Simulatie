import numpy as np
import matplotlib.pyplot as plt

# Parameters
shape = 0.75  # Shape parameter (a)
scale = 2431  # Scale parameter
loc = 16147  # Location parameter

MAX = 11_000

# Generate gamma distribution
data = MAX - np.random.gamma(shape, scale, 1_000_000)

# Plot histogram for visualization (optional)
plt.hist(data, bins=100, density=True, alpha=0.6, color='g')
plt.title('Gamma Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.xlim(0, MAX + 0.1 * MAX)
plt.show()
