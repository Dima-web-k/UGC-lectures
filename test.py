# поиск папок в папке=поиск каталогов в каталоге
import os
pth = r'd:\\'
folders = [e for e in os.listdir(pth) if os.path.isdir(pth + e)]
print(folders)