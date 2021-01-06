import xml.etree.ElementTree as ET
import os

for filename in os.listdir('.'):
	if not filename.endswith('.xml'): continue
	fullname = os.path.join('.', filename)
	tree2 = ET.parse(fullname)
	tree = tree2.getroot()
	tree[3][0].text = 'Pugno'
	tree2.write(filename)