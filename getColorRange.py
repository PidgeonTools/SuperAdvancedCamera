from PIL import Image
import numpy as np


def read_color_blocks(image_path):
    # Load the image using PIL
    img = Image.open(image_path)
    img_array = np.array(img)

    # Initialize the result tuple
    result = []

    # Loop through rows of red, green, and blue blocks (2nd, 5th, and 8th rows)
    for row in [1, 4, 7]:
        color_values = []

        # Loop through each color channel (R, G, B)
        for channel in range(3):
            channel_values = []

            # Loop through each block in the row
            for col in range(11):
                x, y = col * 100, row * 100

                # Get the color value for the block
                block_value = img_array[y:y+100, x:x+100, channel]

                # Average the value over the block to reduce noise
                avg_value = np.mean(block_value)

                # Normalize the value to the 0-1 range and keep up to 5 decimal places
                normalized_value = round(avg_value / 255, 4)

                # Append the value to the channel_values list
                channel_values.append(normalized_value)

            # Append the channel values to color_values
            color_values.append(channel_values)

        # Append color_values to result
        result.append(color_values)

    # Convert the result to a tuple and return
    return tuple(result)


# Test the function
# Note: Please upload a 1100x1100 image that fits the description before running this cell.
image_path = "S:\\Animation\\BlenderScripts\\addons\\SuperAdvancedCamera\\filters\\Color Calibration Snappy.png"
read_color_blocks(image_path)
