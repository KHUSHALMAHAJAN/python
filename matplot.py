import numpy as np
import matplotlib.pyplot as plt  # Correct alias for Matplotlib

arr = [3, 7, 9, 12, 25]  # Use a list instead of a set
a = np.array(arr)  # Convert list to a NumPy array

plt.plot(a)  # Plot the array
plt.show()  # Display the plot
