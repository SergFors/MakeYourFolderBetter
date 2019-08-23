'''
MakeYourFolderBetter v0.1.3
Licensed by Intersog.
'''
import configparser
import json
import os
import time
import shutil
import webbrowser
import tkinter as tk
from datetime import datetime

from handlers import remove, convert, copyfile, info, makedir

config = configparser.ConfigParser()
config.read('config.ini')

def check(count):
    result = ''
    for file in os.listdir():
        if file not in config['DEFAULT']['ignore'] and file not in config['cache']['file']:
            result_loc, info_file = info(file)
            if file.endswith('.jpg'):
                makedir('png')
                result_loc = 'Detect file: ' + file + '. Convert to PNG.'
                convert(file)
            elif file.endswith('.c') or file.endswith('.cpp'):
                result_loc = 'Detect file: ' + file + '. Deleted.'
                remove(file)
            elif os.path.isdir(file):
                try: 
                    os.rmdir(file)
                    result_loc += 'Detect new folder: ' + file + '. She is empty, so app deleted her. Sorry.'
                except OSError: 
                    pass
            elif file.endswith('.html'):
                result_loc = 'Detect file: ' + file
                result_loc += copyfile(file, makedir('html')+file)
                print(copyfile(file, makedir('html')+file))
                result_loc += '\nOpen in in browser.'
                print(os.path.abspath('html/'+file))
                webbrowser.open('file:///' + os.path.abspath('html/'+file))
                config.set('cache','file',file)
            else:
                result_loc = 'Detect file: ' + file + '. Just move it in desired folder.'
                result_loc += copyfile(file, makedir(file.split('.')[-1])+file)
                if copyfile(file, makedir(file.split('.')[-1])+file) != '':
                    config.set('cache','file',file)
            if result_loc != '':
                result += result_loc + '\n'
    if result != '':
        label['text'] += '\n' + str(datetime.now().time()) + ' ' + result
    root.after(5000, check, count+1)

root = tk.Tk()
root.geometry("{2}x{0}+{1}+{3}".format(
    root.winfo_screenheight(), 
    root.winfo_screenwidth()-500, 
    config['DEFAULT']['width'],
    config['DEFAULT']['plus_height']))

label = tk.Label(root, text=config['DEFAULT']['start'])
label.pack()

check(config["DEFAULT"]["count_check"])

root.mainloop()