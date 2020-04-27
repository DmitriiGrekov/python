import os
os.chdir('/home/dmitrii/Документы')



for folderNames,subfolders,filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.endswith('.mp3'):
            print(filename)
