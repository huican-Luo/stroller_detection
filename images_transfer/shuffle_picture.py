import numpy as np
import os
import shutil
import random
'''
#image_list = os.listdir('F:\stroller_dection\images_transfer\png')  # list of images
#label_list = os.listdir('F:\stroller_dection\images_transfer/txt')  # list of labels
def get_file_all_path(path, filetype):
    files = []
    for file in os.listdir(path):
        if file.endswith(filetype):
            temp_path = os.path.join(path, file)
            files.append(temp_path)
    return files
image_list = get_file_all_path('F:\stroller_dection\images_transfer\png','.png')
label_list = get_file_all_path('F:\stroller_dection\images_transfer/txt','.txt')
temp = np.array([image_list, label_list])
temp = temp.transpose()
np.random.shuffle(temp)
print(temp)
images = temp[:, 0]  # array of images   (N,)
labels = temp[:, 1]
#print(image_list)
#print(images,labels)
for png in images:
    shutil.copy(str(png), "F:\stroller_dection\images_transfer\png_txt_shuffle")#将路径下的文件复制到另一个路径下，可以进行替换
for label in labels:
    shutil.copy(str(label), "F:\stroller_dection\images_transfer\png_txt_shuffle")#将路径下的文件复制到另一个路径下，可以进行替换
'''
image_list = os.listdir('F:\stroller_dection\images_transfer\png1')  # list of images
label_list = os.listdir('F:\stroller_dection\images_transfer/txt1')  # list of labels
ran_num = random.sample(range(0,535),535)
file_type1 = '.png'
file_type2 = '.txt'
i = 0
print(image_list)
print(label_list)
for filename in image_list:
    portion = os.path.splitext(filename)
    print(portion)
    if portion[1] == file_type1:
        new_index_image = str(ran_num[i]) + file_type1
        print(new_index_image)
        os.rename('F:\stroller_dection\images_transfer/png1/'+filename,'F:\stroller_dection\images_transfer/png2/'+new_index_image)
        i += 1
j=0
for filename in label_list:
    portion = os.path.splitext(filename)
    if portion[1] == file_type2:
        new_index_label = str(ran_num[j]) + file_type2
        print(new_index_label)
        os.rename('F:\stroller_dection\images_transfer/txt1/'+ filename,'F:\stroller_dection\images_transfer/txt2/'+new_index_label)
        j += 1