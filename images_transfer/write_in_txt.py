txt_file = 'F:\object_dection\stroller_detection\images_transfer/valid.txt'

with open(txt_file,'w') as f:
    for i in range(453,566):
        i_str = str(i)
        file_name = 'F:\object_dection\stroller_detection\images_transfer\stroller_model_construction_yolov7\images/valid/' + i_str+ '.png'
        f.write(file_name + '\n')
f.close()
