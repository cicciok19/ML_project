import tensorflow as tf
import pandas
import numpy as np
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/franc/Documents/GitHub/models/research/object_detection/utils')

import dataset_util


'''flags = tf.compat.v1.flags
flags.DEFINE_string('output_path')
FLAGS = flags.FLAGS'''


def create_tf_example(example):
  height = 144
  width = 256
  filename = example.image_name
  path = "../prova_final_data_3/prova_final_data_3/" + filename
  image = tf.keras.preprocessing.image.load_img(path)
  image= tf.keras.preprocessing.image.img_to_array(image)
  #encoded_image_data = tf.io.encode_jpeg(image) # Encoded image bytes
  encoded_image_data = image.tobytes()
  image_format = b'jpeg'

  xmins = [example.xmin/256] # List of normalized left x coordinates in bounding box (1 per box)
  xmaxs = [example.xmax/256] # List of normalized right x coordinates in bounding box
             # (1 per box)
  ymins = [example.ymin/144] # List of normalized top y coordinates in bounding box (1 per box)
  ymaxs = [example.xmin/144] # List of normalized bottom y coordinates in bounding box
             # (1 per box)
  label = b'Pugno' if example.class_id==2 else b'Mano_aperta'
  classes_text = [label] # List of string class name of bounding box (1 per box)
  classes = [example.class_id] # List of integer class id of bounding box (1 per box)

  tf_example = tf.train.Example(features=tf.train.Features(feature={
      'image/height': dataset_util.int64_feature(height),
      'image/width': dataset_util.int64_feature(width),
      'image/filename': dataset_util.bytes_feature(filename.encode()),
      'image/source_id': dataset_util.bytes_feature(filename.encode()),
      'image/encoded': dataset_util.bytes_feature(encoded_image_data),
      'image/format': dataset_util.bytes_feature(image_format),
      'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
      'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
      'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
      'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
      'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
      'image/object/class/label': dataset_util.int64_list_feature(classes),
  }))
  return tf_example


def main(_):
  writer = tf.compat.v1.python_io.TFRecordWriter("output")

  # TODO(user): Write code to read in your dataset to examples variable
  rows = pandas.read_csv("../labels.csv")
  examples = rows.iterrows()
  for n, example in examples:
  	print(example)
  	break

  for n, example in examples:
  	tf_example = create_tf_example(example)
  	writer.write(tf_example.SerializeToString())


  writer.close()


if __name__ == '__main__':
  tf.compat.v1.app.run()
