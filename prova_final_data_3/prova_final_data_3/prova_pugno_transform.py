import xml.etree.ElementTree as ET
import pandas as pd
from PIL import Image, ImageDraw
import time
import os

data_pd = []

path = 'pugno/'
for filename in os.listdir(path):
	n = {}
	if not filename.endswith('.xml'): continue
	fullname = os.path.join(path, filename)
	tree = ET.parse(fullname).getroot()
	n['image'] = tree[1].text
	n['width'] = tree[2][0].text
	n['height'] = tree[2][1].text
	n['x1'] = int(tree[3][4][0].text)
	n['y1'] = int(tree[3][4][1].text)
	n['x2'] = int(tree[3][4][2].text)
	n['y2'] = int(tree[3][4][3].text)
	data_pd.append(n)

#new = pd.DataFrame.from_records([s for s in data_pd])
#print(new)

for image in data_pd:
	img = Image.open('pugno/'+image['image'])
	width, height = img.size
	draw = ImageDraw.Draw(img, 'RGBA')
	draw.rectangle(((image['x1'], image['y1']), (image['x2'], image['y2'])), outline=(0, 0, 0, 127), width=3)
	img.show()
	time.sleep(3)
