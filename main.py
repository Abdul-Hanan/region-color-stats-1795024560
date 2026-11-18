import cv2
import numpy as np
import os

def create_synthetic_image(width=500, height=500):
    """
    Generates a synthetic color image with gradients to ensure variance
    across all channels.
    """
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # Blue channel: Horizontal gradient from dark to light blue
    img[:, :, 0] = np.linspace(0, 255, width, dtype=np.uint8)

    # Green channel: Vertical gradient from dark to light green
    img[:, :, 1] = np.linspace(0, 255, height, dtype=np.uint8).reshape(-1, 1)

    # Red channel: Combination of horizontal and vertical to create a diagonal-like gradient
    # Ensure values stay within 0-255 range after addition
    red_h = np.linspace(0, 150, width, dtype=np.uint8)
    red_v = np.linspace(0, 150, height, dtype=np.uint8).reshape(-1, 1)
    img[:, :, 2] = np.clip(red_h + red_v, 0, 255)

    return img

def main():
    """
    Main function to generate an image, draw a square, calculate variance,
    and save outputs.
    """
    print("Starting Region Color Stats project...")

    # 1. Generate a synthetic image
    image_width = 600
    image_height = 400
    original_image = create_synthetic_image(image_width, image_height)
    print(f"Generated a {image_width}x{image_height} pixel synthetic image.")

    # Make a copy for drawing the square, keep original for variance calculation
    image_with_square = original_image.copy()

    # 2. Define the central square's parameters
    square_size = 100
    if square_size > min(image_width, image_height):
        print(f"Warning: Square size {square_size} is larger than image dimension. Adjusting.")
        square_size = min(image_width, image_height) // 2

    # Calculate top-left and bottom-right coordinates for the square
    # Ensure coordinates are integers
    center_x, center_y = image_width // 2, image_height // 2
    half_square = square_size // 2

    x1 = int(center_x - half_square)
    y1 = int(center_y - half_square)
    x2 = int(center_x + half_square)
    y2 = int(center_y + half_square)

    # Adjust for odd square sizes to ensure exact size
    x2 = x1 + square_size
    y2 = y1 + square_size

    print(f"Defined a central square of size {square_size}x{square_size} at [{x1}:{x2}, {y1}:{y2}].")

    # 3. Draw the fixed-size square in the center on the copy
    square_color = (0, 0, 255)  # Blue color for the square border (BGR)
    square_thickness = 2
    cv2.rectangle(image_with_square, (x1, y1), (x2, y2), square_color, square_thickness)
    print("Square drawn on the image.")

    # 4. Extract the Region of Interest (ROI) from the *original* image
    roi = original_image[y1:y2, x1:x2]
    print(f"Extracted ROI of shape: {roi.shape}")

    if roi.size == 0:
        print("Error: ROI is empty. Check square coordinates and image dimensions.")
        return

    # 5. Calculate individual pixel intensity variance for B, G, R channels
    # OpenCV stores images in BGR format
    b_channel = roi[:, :, 0]
    g_channel = roi[:, :, 1]
    r_channel = roi[:, :, 2]

    var_b = np.var(b_channel)
    var_g = np.var(g_channel)
    var_r = np.var(r_channel)

    print("\n--- Pixel Intensity Variance within Central Square ---")
    print(f"Blue Channel Variance: {var_b:.2f}")
    print(f"Green Channel Variance: {var_g:.2f}")
    print(f"Red Channel Variance: {var_r:.2f}")
    print("------------------------------------------------------")

    # 6. Save the visual output to a file
    output_filename = "output_image_with_square.png"
    cv2.imwrite(output_filename, image_with_square)
    print(f"\nVisual output saved to '{output_filename}'")

    print("\nProject finished successfully.")

if __name__ == "__main__":
    main()