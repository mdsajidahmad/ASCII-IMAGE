# '''City Street Traffic Speed Analysis
# ● From: Minor 1 – EDA
# ● Extension: Analyze speed variations → congestion zones
# ● Add-ons: Line plots, heatmaps
# ● Difficulty: Medium'''
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# data = {
#     'Street': ['MG Road', 'MG Road', 'MG Road', 'Ring Road', 'Ring Road', 'Ring Road',
#           'Station Road', 'Station Road', 'Station Road'],
#     'Hour': [8, 14, 18, 8, 14, 18, 8, 14, 18],
#     'Average_Speed': [18, 35, 20, 22, 45, 25, 15, 30, 18]
# }
# df = pd.DataFrame(data)
# df
# df.info()
# df.describe()
# plt.figure(figsize=(8,5))
# for street in df['Street'].unique():
#     street_data = df[df['Street'] == street]
#     plt.plot(street_data['Hour'], street_data['Average_Speed'], marker='o', label=street)
# plt.xlabel("Hour of Day")
# plt.ylabel("Average Speed (km/h)")
# plt.title("Traffic Speed Variation Over Time")
# plt.legend()
# plt.grid(True)
# plt.show()
# pivot_table = df.pivot(index='Street', columns='Hour', values='Average_Speed')
# plt.figure(figsize=(7,4))
# sns.heatmap(pivot_table, annot=True, cmap='Reds')
# plt.title("Traffic Congestion Heatmap")
# plt.xlabel("Hour")
# plt.ylabel("Street")
# plt.show()
# def congestion_level(speed):
#     if speed < 20:
#         return 'High Congestion'
#     elif speed <= 40:
#         return 'Moderate Traffic'
#     else:
#         return 'Free Flow'
# df['Congestion_Level'] = df['Average_Speed'].apply(congestion_level)
# df
'''minor project two '''
# from PIL import Image
# import os
# Load the image (correct path)
# img = Image.open(r"D:\sajid\hema_malini.jpg.jpg")
# Resize for ASCII output
# width, height = img.size
# aspect_ratio = height / width
# new_width = 100
# new_height = int(aspect_ratio * new_width * 0.55)
# img = img.resize((new_width, new_height))
# img = img.convert("L")
# chars = "@#%*+=-:."
# pixels = img.getdata()
# ascii_str = "".join(chars[p // 32] for p in pixels)
# ascii_img = "\n".join(
#     ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)
# )
# print(ascii_img)
# with open("ascii_output.txt", "w") as f:
#     f.write(ascii_img)
# print("ASCII art saved to ascii_output.txt")
'''minor project two '''
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

