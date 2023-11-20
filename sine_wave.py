# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Function to plot a sine wave
def plot_sine_wave(frequency, duration, sampling_rate):
    # Generate time values
    t = np.arange(0, duration, 1 / sampling_rate)

    # Generate sine wave
    y = np.sin(2 * np.pi * frequency * t)

    # Plot the sine wave
    plt.plot(t, y)
    plt.title(f"Sine Wave - Frequency: {frequency} Hz")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.show()

# Example usage
if __name__ == "__main__":
    frequency = 7  # Change this to the desired frequency
    duration = 1    # Duration of the sine wave in seconds
    sampling_rate = 1000  # Number of samples per second

    plot_sine_wave(frequency, duration, sampling_rate)
