import shutil
import glob
import os
import os.path

print("Hey There! Please type in the directory you want to arrange!")
user_directory = input()

if os.path.exists(user_directory) == True:
    source = '%s/' % user_directory
    mydict = {
        '/home/ehren/Pictures': ['jpg', 'png', 'gif', 'svg'],
        '/home/ehren/Documents': ['doc', 'docx', 'pdf', 'xls', 'txt', 'zip'],
        '/home/ehren/Music': ['mp3', 'wav', 'pdf', 'xls', 'txt', 'deb']
    }
    for destination, extensions in mydict.items():
        for ext in extensions:
            for file in glob.glob(source + '*.' + ext):
                print("Arranging your files")
                print(file)
                shutil.move(file, destination)
    print("Done!")
else:
    print("""
Invalid Path! Here Are The things you can do to fix this Error:
    
    * Be sure if the path exsists.
    * If you have qoatation marks around your path, please remove them!
    * Be sure the path is on your computer.
    
Non of these work? Be sure to post it as a issue on our github page.

***WARNING THIS IS A BETA SO PLEASE EXPECT THESE ERRORS YOU CAN POST THIS AS A ISSUE ON
OUR GITHUB PAGE! WANT TO JOIN THE DEVELOPMENT VISIT THE GITHUB PAGE!***

Github Page: https://github.com/Ehren12/Automat""")
