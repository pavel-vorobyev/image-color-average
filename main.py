from PIL import Image

image_path = input("Enter path to the image: ")
image = Image.open(image_path)
width, height = image.size

total_r = 0
total_g = 0
total_b = 0

for w in range(width):
    for h in range(height):
        r, g, b = image.getpixel((w, h))
        total_r += r
        total_g += g
        total_b += b

divider = width * height

final_r = int(total_r / divider)
final_g = int(total_g / divider)
final_b = int(total_b / divider)
hex = "#%02x%02x%02x" % (final_r, final_g, final_b)

print("RGB: {}, {}, {}".format(final_r, final_g, final_b))
print("HEX: {}".format(hex))
