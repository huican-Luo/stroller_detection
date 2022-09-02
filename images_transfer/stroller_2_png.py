import shutil
import os
def get_file_all_path(path, filetype):
    files = []
    for file in os.listdir(path):
        if file.endswith(filetype):
            temp_path = os.path.join(path, file)
            files.append(temp_path)
    return files
png_file = get_file_all_path("F:\object_dection\stroller_detection\images_transfer\stroller",'.png')
#print(png_file)
for png in png_file:
    shutil.copy(str(png), "F:\object_dection\stroller_detection\images_transfer\png1")#将路径下的文件复制到另一个路径下，可以进行替换
#print(txt_file)