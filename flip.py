import cv2
import os
import os.path as osp

file_path = '/home/whale/下载/prox_dataset/quantitative/recordings/vicon_03301_01'

base_name = osp.basename(file_path)

color_dir = osp.join(file_path, 'Color')

result_folder = '/home/whale/下载/shujuchuli'
output_folder = osp.join(result_folder, base_name)

if not osp.exists(output_folder):
    os.makedirs(output_folder)


def flip(image):
    out_path = osp.join(output_folder, image)
    img_read = cv2.imread(image)
    img_out = cv2.flip(img_read, 1)
    cv2.imwrite(out_path, img_out)
    print(out_path)


for filename in os.listdir(color_dir):
    img = osp.join(color_dir, filename)
    flip(img)
