import os
import sys
import os.path


def del_xml(path):
    if os.path.isdir(path):
        file = os.listdir(path)
        for xml in file:
            if xml[-4:len(xml)]=='.xml':
                os.remove(os.path.join(path,xml))

def file_path(path):
    if os.path.isdir(path):
        file = os.listdir(path)
        for xml in file:
            if xml =='Figures':
                del_xml(os.path.join(path,xml))
            else:
                file_path(os.path.join(path,xml))

if __name__ == '__main__':

    path = r'D:\ziliao\中国2020热点油气田'
    file_path(path=path)

