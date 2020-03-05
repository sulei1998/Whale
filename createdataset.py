import os
import os.path as osp
import shutil
import sys

recording_folder = '/media/whale/My Passport/111/recordings'
dataset = '/home/whale/下载/prox_dataset/Rehabilitation_dataset'

for filename in os.listdir(dataset):
    origin_folder = osp.join(recording_folder, filename) # /media/whale/My Passport/111/recordings/MPH8_00034_01
    result_folder = osp.join(dataset, filename) # /home/whale/下载/prox_dataset/ceshi/MPH8_00034_01
    color_folder = osp.join(result_folder, 'Color') # /home/whale/下载/prox_dataset/ceshi/MPH8_00034_01/Color
    for name in os.listdir(origin_folder):
        if name == 'Calibration.txt':
            shutil.copy(osp.join(origin_folder, name), osp.join(dataset, filename))
        else:
            out_folder = osp.join(result_folder, name)
            if not osp.exists(out_folder):
                os.makedirs(out_folder)
            for img_name in os.listdir(color_folder):
                img = osp.splitext(img_name)[0]
                if name == 'Skeleton':
                    find_json = osp.join(origin_folder, name, img + '.json')
                    shutil.copy(find_json, osp.join(result_folder, name))
                elif name == 'Color':
                    pass
                else:
                    find_png = osp.join(origin_folder, name, img + '.png')
                    shutil.copy(find_png, osp.join(result_folder, name))




