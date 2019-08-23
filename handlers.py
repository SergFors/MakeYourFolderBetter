import os
import shutil

from PIL import Image

def remove(file):
    os.remove(file)

def convert(file):
    im = Image.open(file)
    im.save('png/' + file[:-4] + '.png')
    remove(file)

def copyfile(file, to):
    if os.path.isfile(to) == False:
        try: shutil.copyfile(file, to)
        except FileNotFoundError: pass
        remove(file)
        return ''
    else: return '\nFile is does exist in folder. \nRename him and before that we try move it again.'

def info(file):
    info_file = []
    info_file.append(file)
    info_file.append(os.path.getmtime(file))
    return ('', info_file)

def makedir(name):
    if not os.path.exists(name):
        os.makedirs(name)
    return (name+'/')