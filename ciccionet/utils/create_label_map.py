ANNOTATION_PATH = '../annotations'

labels = [{'name':'Pugno', 'id':1}, {'name':'Mano_aperta', 'id':2}]

with open(ANNOTATION_PATH + '/label_map.pbtxt', 'w') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')