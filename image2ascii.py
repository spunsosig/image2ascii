import os
import sys
from PIL import Image, ImageOps

def main(image, name):
    size = (150, 150)
    img = Image.open(image)

    img = img.convert('RGB')
    img = ImageOps.contain(img, size)

    width, height = img.size
    print(f"image size = {width} x {height}")
    filepath = fr"C:\Users\ikram\PycharmProjects\image2ascii\ascii\{name}"

    output = []
    for i in range(height):
        output.append(["x"] * width)

    for x in range(0, width):
        for y in range(0, height):

            pixelRGB = img.getpixel((x, y))
            r,g,b = pixelRGB
            brightness = sum([r, g, b])/3

            if brightness == 0:
                output[y][x] = "."
            elif 0 < brightness <= 15:
                output[y][x] = ":"
            elif 15 < brightness <= 30:
                output[y][x] = "("
            elif 30 < brightness <= 45:
                output[y][x] = ")"
            elif 45 < brightness <= 60:
                output[y][x] = "["
            elif 60 < brightness <= 75:
                output[y][x] = "]"
            elif 75 < brightness <= 90:
                output[y][x] = "/"
            elif 90 < brightness <= 105:
                output[y][x] = "!"
            elif 105 < brightness <= 120:
                output[y][x] = ">"
            elif 120 < brightness <= 135:
                output[y][x] = "<"
            elif 135 < brightness <= 150:
                output[y][x] = "~"
            elif 150 < brightness <= 165:
                output[y][x] = "&"
            elif 165 < brightness <= 180:
                output[y][x] = "@"
            elif 180 < brightness <= 195:
                output[y][x] = "*"
            elif 195 < brightness <= 210:
                output[y][x] = "#"
            elif 225 < brightness <= 240:
                output[y][x] = "%"
            elif 240 < brightness <= 255:
                output[y][x] = "$"

        output_file = open(filepath, "w")

    for row in output:
        output_file.write("".join(row)+"\n")

    os.startfile(filepath)
    output_file.close()

if __name__ == "__main__":
    try:
        main(sys.argv[1], sys.argv[2])
        print(f"ASCII '{sys.argv[2]}' created successfully!")
    except:
        print("An exception occurred")
