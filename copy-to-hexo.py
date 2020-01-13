import os
from shutil import copyfile
from_path = r"/home/rieunity/Documents/Notes" # 原路经
to_path = r"/home/rieunity/blog/source/download/Notes" # 目标路径
filetype = '.pdf' # 需要复制的文件类型
def copy_pdf(from_path, to_path, filetype):
    length = (len(from_path))
    for root, dirs, files in os.walk(from_path):
        dest_dir = os.path.join(to_path,root[length:][1:])
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for file in files:
            if os.path.splitext(file)[1] == filetype:
                from_path = os.path.join(root,file)
                relative_path = (from_path[length:])
                dest_path  = os.path.join(to_path,relative_path[1:]) 
                copyfile(from_path, dest_path)
copy_pdf(from_path, to_path, filetype)
copy_pdf(from_path, to_path, '.md')
print("All the files in " + from_path + " has been copied successfully!")