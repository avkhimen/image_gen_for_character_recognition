# Imports PIL module
from PIL import Image
from PIL import ImageDraw
 
# creating a image object (new image object) with
# RGB mode and size 200x200
img = Image.new(mode="RGB", size=(200, 200), color='white')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
 
# Add Text to an image
I1.text((40, 40), "Random Name", fill=(0, 0, 0))
I1.text((40, 60), "SFDDFGFDGDG", fill=(0, 0, 0))
I1.text((40, 80), "DFGDHDFHDGH", fill=(0, 0, 0))

img.save('test.png', 'PNG')
