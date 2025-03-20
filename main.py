import imageio
import numpy as np
import matplotlib.pyplot as plt

# Create a list to store frames
frames = []

# Generate a few frames of a moving sine wave
for i in range(50):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + i * 0.1)  # Sine wave moving over time

    # Plot the sine wave
    plt.plot(x, y)
    plt.xlim(0, 2 * np.pi)
    plt.ylim(-1.5, 1.5)
    plt.title(f"Frame {i+1}")

    # Save the plot to a file
    plt.savefig('temp.png')
    plt.clf()  # Clear the plot for the next frame

    # Read the saved image and append to frames
    frames.append(imageio.imread('temp.png'))

# Save the frames as a GIF
imageio.mimsave('sine_wave_animation.gif', frames, duration=0.1)  # 0.1 sec per frame

print("GIF created successfully!")