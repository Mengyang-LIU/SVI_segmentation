# -*- coding:utf-8 -*-

import csv                 
import urllib.request      
import os                  
import socket              

file1 = '/Users/...csv'                        #coordinates of sample points
#file2 = '/Users/../key.csv'                   #multiple key file
outputdir = "/Users/.."                        #folder to save SVIs
baidmap_key = '..'                             #存储申请的ak值，把csv中的key全部放在里面

#i = 1
#k = 0                                         #对应列表下标
"""
with open(file2) as csvfile1:                  #打开存有key的文件file2，并将文件对象存储在csvfile1中
    csvreader1 = csv.DictReader(csvfile1)      #接收文件对象，并创建一个与文件相关的DictReader对象
    for row in csvreader1:                     #遍历文件中各行
        baimap_key.append(row['key'])          #将文件中的一行数据追加到列表baimap_key尾部
"""
with open(file1) as csvfile:                   #打开file1，并将文件对象存储在csvfile中，创建相应的DictReader对象
    csvreader=csv.DictReader(csvfile)
    for row in csvreader:
        colume1=row['lan']
        colume2=row['lon']
        position = [str(colume1), str(colume2)]     #遍历文件中各行，将经纬度坐标存入变量position中

      #  if i%100==0:        #i%1000看余数，看等不等于0，只有1000/2000/3000余数才会为0
      #      k=k+1
        key= baidmap_key      #update the next key if the current usage is used up

        name_1 = str(row['TARGET_FID']) + "_180.bmp"                      #update the image name
        name_2 = str(row['TARGET_FID']) + "_360.bmp"

        if os.path. exists(outputdir) is False:     #create new folder
            os.mkdir(outputdir)

        try:                                        #access the SVI of each sample point
            url = "http://api.map.baidu.com/panorama/v2?ak=" + key\
            +"&width=1024&height=512&location=" + str(position[0]) + "," + str(position[1])\
            +"&fov=180/&heading=180"+"/&coordtype=wgs84ll" # "fov" change for different angle of view
            print(url)
            socket. setdefaulttimeout(10)
            urllib. request. urlretrieve(url, os.path.join(outputdir, name_1))

            url1 = "http://api.map.baidu.com/panorama/v2?ak=" + key \
                  + "&width=1024&height=512&location=" + str(position[0]) + "," + str(position[1]) \
                  + "&fov=180/&heading=360" + "/&coordtype=wgs84ll"
            print(url1)
            socket.setdefaulttimeout(10)
            urllib.request.urlretrieve(url1, os.path.join(outputdir, name_2))

        except Exception as e:
            print(str(e))
           






