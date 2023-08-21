#!/usr/bin/env python3

import matplotlib.pyplot as plt
import json

# load data
with open('chemlab1data.json', 'r') as file:
    data = json.load(file)

xpoints = list(range(1,9))
# initialize variables, is ths even necessary in python?
lor = { "x": xpoints, "y": [] }
wor = { "x": xpoints, "y": [] }
hot = { "x": xpoints, "y": [] }
lob = { "x": xpoints, "y": [] }
wob = { "x": xpoints, "y": [] }
wot = { "x": xpoints, "y": [] }

# organize data
for i in range(len(data)):
    lor["y"].append(data[i]["lor"])
    wor["y"].append(data[i]["wor"])
    hot["y"].append(data[i]["hot"])
    lob["y"].append(data[i]["lob"])
    wob["y"].append(data[i]["wob"])
    wot["y"].append(data[i]["wot"])

# graph data lines
plt.plot(lor["x"], lor["y"], label='Length of Room')
plt.plot(wor["x"], wor["y"], label='Width of Room')
plt.plot(lob["x"], lob["y"], label='Length of Board')
plt.plot(hot["x"], hot["y"], label='Height of Table')
plt.plot(wot["x"], wot["y"], label='Width of Tile')
plt.plot(wob["x"], wob["y"], label='Width of Book')

# graph trend lines

plt.plot(lor["x"], [10204.5] * 8, color='black', linewidth=.5)
plt.plot(wor["x"], [8063.5] * 8, color='black', linewidth=.5)
plt.plot(lob["x"], [5892.5] * 8, color='black', linewidth=.5)
plt.plot(hot["x"], [916.5] * 8, color='black', linewidth=.5)
plt.plot(wot["x"], [305.0] * 8, color='black', linewidth=.5)
plt.plot(wob["x"], [210.0] * 8, color='black', linewidth=.5)

# graph stuff
plt.xlabel('Group Number (#)')
plt.ylabel('Measurements (mm)')

plt.yticks(list(range(0, 11000, 500)))

plt.title('Lab #1 - Classroom Measurement')

plt.legend(loc='center right')

plt.savefig('./chemlab1data.png', format='png', dpi=1200)
