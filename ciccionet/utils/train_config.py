import tensorflow as tf
import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format

CONFIG_PATH = '../ssd_mobilenet/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/pipeline.config'
config = config_util.get_configs_from_pipeline_file(CONFIG_PATH)

pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
with tf.io.gfile.GFile(CONFIG_PATH, "r") as f:                                                                                                                                                                                                                     
    proto_str = f.read()                                                                                                                                                                                                                                          
    text_format.Merge(proto_str, pipeline_config)

batch_size = 32

pipeline_config.model.ssd.num_classes = 2
pipeline_config.train_config.batch_size = batch_size
pipeline_config.train_config.fine_tune_checkpoint = 'ssd_mobilenet/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/checkpoint/ckpt-0'
pipeline_config.train_config.fine_tune_checkpoint_type = "detection"
pipeline_config.train_input_reader.label_map_path= 'annotations/label_map.pbtxt'
pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = ['annotations/train.record']
pipeline_config.eval_input_reader[0].label_map_path = 'annotations/label_map.pbtxt'
pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = ['annotations/test.record']
pipeline_config.train_config.optimizer.momentum_optimizer.learning_rate.cosine_decay_learning_rate.learning_rate_base = 0.04
pipeline_config.train_config.optimizer.momentum_optimizer.learning_rate.cosine_decay_learning_rate.warmup_learning_rate = 0.00726666

config_text = text_format.MessageToString(pipeline_config)                                                                                                                                                                                                        
with tf.io.gfile.GFile(CONFIG_PATH, "wb") as f:                                                                                                                                                                                                                     
    f.write(config_text)

print(f'Generated config with batch_size {batch_size}, learning rate 0.04 and warm_up lr 0.00726666')

