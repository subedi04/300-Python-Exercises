'''
Write a Python Program to Rotate an image: Using another method
'''

from PIL import Image

def rotate_image(input_path, output_path, degrees):
    try:
        # Open the image file
        image = Image.open(input_path)

        # Rotate the image by the specified degrees
        rotated_image = image.rotate(degrees)

        # Save the rotated image to the output path
        rotated_image.save(output_path)

        print(f"Image rotated by {degrees} degrees and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_path = "input.jpg"  # Replace with your input image file path
    output_path = "output.jpg"  # Replace with your output image file path
    degrees = 90  # Specify the rotation angle (e.g., 90 degrees)

    rotate_image(input_path, output_path, degrees)
