import colorgram

colors = colorgram.extract('image.jpg', 30)
rgb_list = []

# Store the rgb values in a tuple 
rgb_list = [tuple(color.rgb) for color in colors]
print(rgb_list)
