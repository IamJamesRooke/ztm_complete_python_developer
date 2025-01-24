from PIL import Image
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'Pokedex', 'pikachu.jpg')

try:
    img = Image.open(image_path)
    print(f'Successfully opened image: {img.size}')  # This will print the dimensions if successful
    img.show()  # This line is now uncommented to display the image
except FileNotFoundError:
    print(f'File not found - please check that the file exists at {image_path}')
except Exception as e:
    print(f'Error opening image: {e}')