from tkinter import filedialog
import os
import shutil

def findFolder(source):
    aux = source.split("\\")
    count = 0
    _list = []
    for x in aux:
        if (x == 'Imagens'):
            if aux[count+1]:
                _list.append(aux[count-1])
                _list.append(aux[count+1])
                return [aux[count-1],aux[count+1]]
        count += 1

def main():
    folder = filedialog.askdirectory()
    for root,dirs,files in os.walk(folder):
        for file in files:
            source = os.path.join(os.path.realpath(root), file)
            destination = os.path.join(os.path.realpath(folder), file)
            name = findFolder(source)
            if (name):
                if "." not in name[1]:
                    destination = os.path.join(os.path.realpath(folder), name[1]+"-"+name[0]+"-"+file)
                else:
                    destination = os.path.join(os.path.realpath(folder), name[0]+"-"+file)
            shutil.move(source,destination)

if __name__ == '__main__':
    main()
    