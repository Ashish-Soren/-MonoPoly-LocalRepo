# Find Mean, Median , Mode of a continuous series

import numpy as np
from scipy import stats

# Define the class intervals and frequencies
class_intervals = [0, 10, 20, 30, 40, 50, 60, 70]
frequencies = [6, 8, 20, 25, 15, 10, 4]

# Calculate midpoints of each class interval
midpoints = [(class_intervals[i] + class_intervals[i+1]) / 2 for i in range(len(class_intervals) - 1)]

# Calculate the mean
mean = np.sum(np.array(midpoints) * np.array(frequencies)) / np.sum(frequencies)

# Calculate the median
cumulative_frequency = np.cumsum(frequencies)
median_class_index = np.argmax(cumulative_frequency > np.sum(frequencies) / 2)
median_class = class_intervals[median_class_index]
median = median_class + (class_intervals[median_class_index + 1] - median_class) * (np.sum(frequencies) / 2 - cumulative_frequency[median_class_index - 1]) / frequencies[median_class_index]

# Calculate the mode
mode = stats.mode(midpoints)[0][0]

print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Mode: {mode}")