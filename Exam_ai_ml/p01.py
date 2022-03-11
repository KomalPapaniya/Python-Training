import os
import random
import string

path_file = open('path.txt','w')

path = "C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\Exams\\Exam"

if __name__ == "__main__":

    for (root,dirs,files) in os.walk(path):
        for file in files:
            # if file.endswith(".txt"):
                path_file.write(os.path.join(root, file))
                path_file.write("\n")
    path_file.close()

# -----------------------------------------------------------------------------------------------------
# generating random strings and creating files

file = open('path.txt', "r")

for line in file:
    extracting_path = line.split("Exam")[-1]
    file_name = extracting_path.replace("\\", "_")
    # print(file_name)
    save_path = 'C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\Exams\\Output'
    completeName = os.path.join(save_path, file_name[:-1])
    name_file = open(completeName,'w')
    name_file.write(''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10))))
    name_file.close()

