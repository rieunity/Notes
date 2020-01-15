import os
from shutil import copyfile
# 设置原路径和目标路径
from_path = r"/home/rieunity/Documents/test" # 原路经
to_path = r"/home/rieunity/Documents/aim" # 目标路径
filetype = '.pdf' # 需要复制的文件类型
def find_pdf(from_path, filetype):
    pdf_dirs = []
    for root, dirs, files in os.walk(from_path):
        for file in files:
            if os.path.splitext(file)[1] == filetype:
                
                absolute_dir = os.path.join(root,file)
                #destination = os.path.join
                length = (len(from_path))
                relative_dir = (absolute_dir[length:]) 
                pdf_dir = []  #一个包含文件绝对路径,相对于原路径的相对文件路径和相对目录路径(去掉文件本身的绝对路径)的三维向量
                pdf_dir.append(absolute_dir)
                pdf_dir.append(relative_dir)
                pdf_dir.append(os.path.split(relative_dir)[0])
                pdf_dirs.append(pdf_dir) #将所有的文件名添加到pdf_dirs列表中
    return pdf_dirs   # 返回pdf_dirs列表
def copy_pdf(to_path,pdf_dirs):
    for pdf_dir in pdf_dirs:
        pdf_dir[1] = pdf_dir[1][1:] # 这里是去掉路径前的第一个斜线,这是os.path.join()函数的要求
        pdf_dir[2] = pdf_dir[2][1:]
        dest_path = os.path.join(to_path,pdf_dir[1]) # 目标文件夹绝对路径
        dest_dir = os.path.join(to_path,pdf_dir[2])  # 目标文件绝对路径
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        if not os.path.exists(dest_path):
            os.mknod(dest_path)
        copyfile(pdf_dir[0],dest_path)

pdf_dirs = find_pdf(from_path,filetype)
copy_pdf(to_path,pdf_dirs)
print("Copy all the files successfully!")