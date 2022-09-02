import os
i=0
for roots, drives, files in os.walk("./"):
    for filename in files:
        file_path=os.path.join(roots,filename)
        extension_name = os.path.splitext(file_path)  # 将文件的绝对路径中的后缀名分离出来
        if extension_name[1] == '.jpg' or extension_name[1]=='.jpeg':
            newfilename=str(i)+".png"
            newpath=os.path.join(roots,newfilename)
            os.rename(file_path, newpath)
            i=i+1
