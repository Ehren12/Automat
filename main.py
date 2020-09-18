import shutil
import glob
import os

source = '/home/ehren/Downloads/'
mydict = {
    '/home/ehren/Pictures': ['jpg','png','gif', 'svg'],
    '/home/ehren/Documents': ['doc','docx','pdf','xls', 'txt'],
    '/home/ehren/Documents': ['mp3','wav','pdf','xls', 'txt']
}
for destination, extensions in mydict.items():
    for ext in extensions:
        for file in glob.glob(source + '*.' + ext):
            print(file)
            shutil.move(file, destination)
