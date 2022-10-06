# How to extract colors from a picture with colorgram.py module in python
import colorgram

rgb_colors = [] 
colors = colorgram.extract('image.jpg', 15)

for color in colors:
    # rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
# Output of the above code 
# [(253, 252, 250), (244, 248, 246), (251, 248, 250), (197, 169, 109), (104, 87, 96), (159, 94, 65), (66, 101, 112), (241, 245, 248), (11, 51, 65), (127, 138, 91), (130, 155, 166), (242, 198, 131), (164, 153, 158), (189, 98, 75), (37, 76, 83)]
# First three shades are of white hence those are removed from our final color list in main2.py