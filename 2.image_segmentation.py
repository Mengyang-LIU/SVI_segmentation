#!--*-- coding:utf-8 --*--

import os
import tarfile
import numpy as np
from PIL import Image
import tensorflow as tf
import time

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"            # juat display warn & error

class DeepLabModel(object):
	# load deepLab model
    INPUT_TENSOR_NAME = 'ImageTensor:0'
    OUTPUT_TENSOR_NAME = 'SemanticPredictions:0'
    FROZEN_GRAPH_NAME = 'frozen_inference_graph'

	# initianize the model settings
    def __init__(self, tarball_path):
        self.graph = tf.Graph()
        graph_def = None
        tar_file = tarfile.open(tarball_path)
        for tar_info in tar_file.getmembers():
            if self.FROZEN_GRAPH_NAME in os.path.basename(tar_info.name):
                file_handle = tar_file.extractfile(tar_info)
                graph_def = tf.GraphDef.FromString(file_handle.read())
                break

        tar_file.close()

        if graph_def is None:
            raise RuntimeError('Cannot find inference graph in tar archive.')

        with self.graph.as_default():
            tf.import_graph_def(graph_def, name='')

        self.sess = tf.Session(graph=self.graph)
	
	# 输入原始图像，返回语义分割结果，格式为数组
    def run(self, image):
        batch_seg_map = self.sess.run(self.OUTPUT_TENSOR_NAME,
                                      feed_dict={self.INPUT_TENSOR_NAME: [np.asarray(image)]})
        seg_map = batch_seg_map[0]
        return seg_map


if __name__ == '__main__':
    # 定义文件路径
    in_dir = r"..\picture_in"          # folder of original SVIs
    out_dir = r"..\picture_out"        # folder for operated images
    model_file = r"..\models\deeplabv3_mnv2_cityscapes_train_2018_02_05.tar.gz"   # trained model
    # model_file = r"..\models\deeplabv3_cityscapes_train_2018_02_06.tar.gz"  

    start_time = int(time.time())       
    MODEL = DeepLabModel(model_file)    # initiate the model
    # loop all the SVIs in the folder
    for img_file in os.listdir(in_dir):
        try:
            st_seg = int(time.time())           # start time
            # open the image
            original_img = Image.open(os.path.join(in_dir, img_file))
            # segmentation
            seg_map = MODEL.run(original_img)
			# transfer the segementation result into the image 
            new_im = Image.fromarray(seg_map.astype('uint8'))
			# save the operated Image
            new_im.save(os.path.join(out_dir, img_file))
			# print the file name of the image and time spent 
            print("{} spend time {}s".format(img_file, int(time.time()) - st_seg))
        except:
			# print the fiile name if an error occurred.
            print("{} FAIL!".format(img_file))
	# calculate the total time spent
    print('spend time %ds' % (int(time.time()) - start_time))