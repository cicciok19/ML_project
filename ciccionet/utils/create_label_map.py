ANNOTATION_PATH = '../annotations'

labels = [{'name':'Pugno', 'id':1}, {'name':'Mano_aperta', 'id':2}, 
			{'name':'Pollice_giu', 'id':3}, {'name':'Pollice_su', 'id':4},
			{'name':'Due_dita', 'id':5}]

with open(ANNOTATION_PATH + '/label_map.pbtxt', 'w') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')