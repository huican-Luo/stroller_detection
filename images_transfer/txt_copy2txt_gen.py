import shutil
import os
def get_file_all_path(path, filetype):
    files = []
    for file in os.listdir(path):
        if file.endswith(filetype):
            temp_path = os.path.join(path, file)
            files.append(temp_path)
    return files
txt_file = get_file_all_path("F:\object_dection\stroller_detection\images_transfer\stroller",'.txt')
print(txt_file)
for txt in txt_file:
    shutil.copy(str(txt), "F:\object_dection\stroller_detection\images_transfer/txt1")#将路径下的文件复制到另一个路径下，可以进行替换
#print(txt_file)