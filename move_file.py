import os
import shutil

from_dir = "C:/Users/prana/OneDrive/Desktop/Project-102"
to_dir = "C:/Users/prana/OneDrive/Desktop/Document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,ext == os.splitext(file_name)

    if ext == " ":
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_files"
        path3 = to_dir + '/' + "Document_files" + '/' + file_name

        if os.path.exists(path2):
            print("Moving " + file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name)
            shutil.move(path1,path3)