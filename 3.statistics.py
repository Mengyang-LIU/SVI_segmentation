# -*- coding:utf-8 -*-

import os
import csv
from PIL import Image
import numpy as np

in_rootdir = r"..\picture_out\picture"       # folder with segemented images
out_file = r"..\picture_out\statistics.csv"     # statistics result 

# current executed number of images, default number is 0
count = 0               
# create csv 
writer = csv.writer(open(out_file, "w", newline=""), dialect=("excel"))  
# colume name
writer.writerow(["pid", "road", "sidewalk", "building", "wall", "fence",
                 "pole", "traffic_light", "traffic_sign", "vegetation", "terrain",
                 "sky", "person", "rider", "car", "truck", "bus", "train", "motorcycle", "bicycle"])
for file in os.listdir(in_rootdir):
	# open the image
    img = Image.open(os.path.join(in_rootdir, file))     
	# current executed number of images +1
    count += 1
    # 初始化每个灰度值的像素数量为0
    count_dic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0,
                 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, -1: 0, 255: 0}
    # 将图像转为矩阵，对灰度值进行统计
    ar = np.array(img).flatten().tolist()
	# 计算灰度值在0-18之间的像素数量，并存储到字典中
    for item in count_dic:
        count_dic[item] = ar.count(item)
    # number of pixels 
    sumcount = len(ar)
	# 计算每个灰度的百分比，并写入CSV中calculate the percentage of each 
    writer.writerow([file.split(".")[0], count_dic[0]*1.0/sumcount, count_dic[1]*1.0/sumcount, count_dic[2]*1.0/sumcount,
                     count_dic[3]*1.0/sumcount, count_dic[4] * 1.0 / sumcount, count_dic[5]*1.0/sumcount,
                     count_dic[6]*1.0/sumcount, count_dic[7]*1.0/sumcount, count_dic[8] * 1.0 / sumcount,
                     count_dic[9]*1.0/sumcount, count_dic[10]*1.0/sumcount, count_dic[11]*1.0/sumcount,
                     count_dic[12]*1.0/sumcount, count_dic[13] * 1.0 / sumcount, count_dic[14]*1.0/sumcount,
                     count_dic[15]*1.0/sumcount, count_dic[16]*1.0/sumcount, count_dic[17]*1.0/sumcount,
                     count_dic[18]*1.0/sumcount])
	# print file name and current executed number of images
    print(file, count)


