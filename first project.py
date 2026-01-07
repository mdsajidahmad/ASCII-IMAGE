'''minor-2 project '''
from PIL import Image
# ----- ASCII CHARACTERS -----
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
img = Image.open(r"D:\sajid\my.jpg.jpeg")
def resize_image(image, new_width=80):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))
def grayify(image):
    return image.convert("L")   # convert image to grayscale
def pixels_to_ascii(image):
    ascii_str = ""
    pixels = image.getdata()
    for pixel in pixels:
        if pixel < 25:
            ascii_str += "@"
        elif pixel < 50:
            ascii_str += "#"
        elif pixel < 75:
            ascii_str += "S"
        elif pixel < 100:
            ascii_str += "%"
        elif pixel < 125:
            ascii_str += "?"
        elif pixel < 150:
            ascii_str += "*"
        elif pixel < 175:
            ascii_str += "+"
        elif pixel < 200:
            ascii_str += ";"
        elif pixel < 225:
            ascii_str += ":"
        else:
            ascii_str += "."
    return ascii_str
# ---- MAIN FUNCTION ----
def image_to_ascii(path):
    try:
        img = Image.open(path)
    except:
        print("Image not found!")
        return
    img = resize_image(img)
    img = grayify(img)
    ascii_str = pixels_to_ascii(img)
    img_width = img.width
    # PRINT + SAVE BOTH
    output_file = "output_ascii.txt"
    with open(output_file, "w") as f:
        for i in range(0, len(ascii_str), img_width):
            line = ascii_str[i:i+img_width]
            print(line)              # print screen par
            f.write(line +"\n")     # file me save
    print("\n✔ ASCII image saved as:", output_file)
image_path = "my.jpg.jpeg"     
image_to_ascii(image_path)

