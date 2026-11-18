# region-color-stats

This project generates a synthetic color image, draws a fixed-size square in its center, then calculates and displays the individual pixel intensity variance for its Blue, Green, and Red color channels solely within that central square. The resulting image with the drawn square is saved to a file, and variance statistics are printed to the console.

**Features:**
- Generates a static color image with gradients.
- Draws a central square without modifying the original data for analysis.
- Calculates BGR pixel intensity variance within the defined square.
- Saves the visual output (image with square) to a file.
- Outputs variance statistics to the console.
- Designed to run on headless servers without a GUI.

**How to Run:**

1.  **Clone the repository (if applicable) or save the files.**
2.  **Install dependencies:**
    Ensure you have `pip` installed. Then, from the project root directory, run:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execute the script:**
    ```bash
    python main.py
    ```

**Output:**
- The script will print the calculated Blue, Green, and Red channel variances to your console.
- An image file named `output_image_with_square.png` will be saved in the same directory, showing the generated image with the central square.