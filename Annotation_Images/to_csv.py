import csv
import os
import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)
root = 'C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\Annotation_Images\\komal\\TNR_LPR_cropped_images'
dirlist = sorted_alphanumeric(os.listdir(root))
# print(dirlist)
with open('lable_part_3.csv', 'w') as obj:
     for filename in dirlist:
         obj.write(filename+','+'\n')