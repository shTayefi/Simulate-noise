import numpy as np
from PIL import Image  # Import Image from Pillow
import matplotlib.pyplot as plt

def add_awgn(image, snr):
    """
    Add Gaussian noise to an image based on a given SNR (Signal-to-Noise Ratio)
    """
    image = image / 255.0  # Normalize image to [0, 1]
    noise = np.random.normal(0, 10**(-snr / 20), image.shape)  # Generate Gaussian noise
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 1)  # Clip values to valid range
    return (noisy_image * 255).astype(np.uint8)  # Rescale back to [0, 255]

# Load the original image
image_path = r"C:\Users\test\image_1.jpg"
original_image = np.array(Image.open(image_path))

# Generate the noisy image
noisy_image = add_awgn(original_image, snr=20)

# Plot the original and noisy images side by side
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title("Original Image")
plt.axis('off')

# Noisy image
plt.subplot(1, 2, 2)
plt.imshow(noisy_image)
plt.title("Noisy Image (SNR=20)")
plt.axis('off')

# Show the comparison
plt.tight_layout()
plt.show()
