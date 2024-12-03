# Simulate-noise
### Adding Gaussian Noise to Images and Visualizing the Results

---

####  Introduction 
This project demonstrates how to add Gaussian noise to an image using Python and visualize the effects by displaying the original and noisy images side-by-side. The noise level is controlled by specifying the Signal-to-Noise Ratio (SNR).

---

####  Features 
- Load and process images in Python using Pillow (`PIL`).
- Add Gaussian noise to an image based on a specified SNR.
- Compare the original and noisy images visually using Matplotlib.

---

####  Installation 

To run the script, ensure you have the required Python libraries installed:

1.  NumPy  (for numerical operations):
   ```
   pip install numpy
   ```

2.  Pillow  (for image manipulation):
   ```
   pip install pillow
   ```

3.  Matplotlib  (for image visualization):
   ```
   pip install matplotlib
   ```

---

####  How to Use 

1.  Clone or Download the Repository 
   Download the code file to your local machine.

2.  Set the Image Path 
   Replace the placeholder file path with the path to your image:
   ```python
   image_path = r"C:\path\to\your\image.jpg"
   ```

3.  Run the Script 
   Use the following command in your terminal or IDE:
   ```
   python script_name.py
   ```

4.  View the Output 
   The script will display two images:
   -  Original Image : The original input image.
   -  Noisy Image : The image with added Gaussian noise (controlled by SNR).

---

####  Code Explanation 

1.  Function: `add_awgn` 
   - Adds Gaussian noise to an image based on a given SNR.
   - Normalizes the image to the `[0, 1]` range before adding noise.
   - Clips the noisy image to valid pixel values and rescales to `[0, 255]`.

   ```python
   def add_awgn(image, snr):
       """
       Add Gaussian noise to an image based on a given SNR (Signal-to-Noise Ratio).
       Args:
           image (np.ndarray): Input image as a NumPy array.
           snr (float): Signal-to-Noise Ratio in decibels (dB).
       Returns:
           np.ndarray: Noisy image.
       """
       image = image / 255.0  # Normalize image
       noise = np.random.normal(0, 10 (-snr / 20), image.shape)  # Generate noise
       noisy_image = image + noise
       noisy_image = np.clip(noisy_image, 0, 1)  # Clip values
       return (noisy_image * 255).astype(np.uint8)
   ```

2.  Loading and Processing the Image 
   - The script uses `Image.open` from Pillow to read an image from the specified path.
   - Converts the image into a NumPy array for processing.

   ```python
   original_image = np.array(Image.open(image_path))
   ```

3.  Displaying the Results 
   - The script uses Matplotlib to plot the original and noisy images side-by-side.

   ```python
   plt.figure(figsize=(10, 5))

   # Original Image
   plt.subplot(1, 2, 1)
   plt.imshow(original_image)
   plt.title("Original Image")
   plt.axis('off')

   # Noisy Image
   plt.subplot(1, 2, 2)
   plt.imshow(noisy_image)
   plt.title("Noisy Image (SNR=20)")
   plt.axis('off')

   plt.tight_layout()
   plt.show()
   ```

---

####  Customization 

1.  Change the SNR :
   Modify the `snr` parameter to adjust the level of Gaussian noise:
   ```python
   noisy_image = add_awgn(original_image, snr=20)  # Change '20' to your desired SNR value
   ```

2.  Use a Different Image :
   Replace the `image_path` with the path to your desired image:
   ```python
   image_path = r"C:\path\to\your\image.jpg"
   ```

---

####  Expected Output 
The script will generate a side-by-side comparison of:
1. The  original image .
2. The  noisy image , which includes added Gaussian noise with the specified SNR.
