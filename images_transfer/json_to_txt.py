"""
import pathlib
a = list(pathlib.Path('F:\图像格式转换\json').glob('*.json'))
print(a)
"""
import json
import os
def get_file_all_path(path, filetype):
    """
    获取当前文件夹下的以.xlsx结尾的文件，不包括子文件夹
    :param path: 路径
    :param filetype:文件类型，如：'.xlsx'
    :return:文件全路径名 列表
    """
    files = []
    for file in os.listdir(path):
        if file.endswith(filetype):
            temp_path = os.path.join(path, file)
            files.append(temp_path)
    return files

json_file = get_file_all_path("F:\object_dection\stroller_detection\images_transfer\images",'.json')

def convert(img_size, box):
     dw = 1. / (img_size[0])
     dh = 1. / (img_size[1])
     x = (box[0] + box[2]) / 2.0
     y = (box[1] + box[3]) / 2.0
     w = box[2] - box[0]
     h = box[3] - box[1]
     x = x * dw
     w = w * dw
     y = y * dh
     h = h * dh
     """
    x1 = box[0]
    y1 = box[1]
    x2 = box[2]
    y2 = box[3]
    """
     return (x, y, w, h)


def decode_json(json_floder_path, json_name):
    txt_name = json_name[0:-5] + '.txt'
    txt_file = open(txt_name, 'w')

    json_path = os.path.join(json_floder_path, json_name)
    data = json.load(open(json_path, 'r', encoding='utf-8'))

    img_w = data['imageWidth']
    img_h = data['imageHeight']

    for i in data['shapes']:

        if (i['shape_type'] == 'rectangle' and i['label'] == 'Positive'):
            x1 = int(i['points'][0][0])
            y1 = int(i['points'][0][1])
            x2 = int(i['points'][1][0])
            y2 = int(i['points'][1][1])

            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write( '0' + " " + " ".join([str(a) for a in bbox]) + '\n')
        else:
            x1 = int(i['points'][0][0])
            y1 = int(i['points'][0][1])
            x2 = int(i['points'][1][0])
            y2 = int(i['points'][1][1])

            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write('1' + " " + " ".join([str(a) for a in bbox]) + '\n')


if __name__ == "__main__":

    json_floder_path = 'F:\object_dection\stroller_detection\images_transfer\images'
    #json_names = os.listdir(json_floder_path)
    for json_name in json_file:
        decode_json(json_floder_path, json_name)