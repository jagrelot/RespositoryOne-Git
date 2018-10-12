#Copyright © 2018 Acumen Solutions, Inc. The Thorax Salesforce Metadata Utility was
#created by Acumen Solutions. Except for the limited rights to use and make copies
#of the Software as provided in a License Agreement, all rights are reserved.

import os
import sys
root = sys.argv[1]

filenames = os.listdir(root + '/temp')
filelist = []
foldertype = ''

for filename in filenames:
    if filename[:4] == 'Temp':
        foldertype = filename[4:]
        foldertype = foldertype.split('.')[0]

    if '.folder' in filename:
        folderlist = []
        dirname = filename.replace('Folder.folder', '')
        if dirname == 'Email':
            dirname = 'EmailTemplate'
        with open(root + '/temp/' + filename) as folderfile:
            for line in folderfile:
                if 'FileName: ' in line:
                    try:
                        foldername = line.split('/', 1)[1]
                    except:
                        foldername = line.replace('FileName: ', '')
                    folderlist.append(foldername)


        with open(root + '/temp/' + dirname + '.processed', 'w+') as processed:
            for line in folderlist:
                processed.write(line)

        os.remove(root + '/temp/' + filename)

    elif 'Temp' + foldertype + '.' in filename:
        foldername = filename.split('.', 1)[1]
        filelist.append('FileName: temp/' + foldername + '\n')
        with open(root + '/temp/' + filename) as documentfile:
            for line in documentfile:
                if 'FileName: ' in line:
                    filelist.append(line)

        os.remove(root + '/temp/' + filename)

if len(filelist) > 0:
    if foldertype == 'EmailTemplate':
        newfile = open(root + '/temp/' + foldertype + '.email', 'w+')
    elif foldertype == 'Report':
        newfile = open(root + '/temp/' + foldertype + '.report', 'w+')
    elif foldertype == 'Dashboard':
        newfile = open(root + '/temp/' + foldertype + '.dashboard', 'w+')
    else:
        newfile = open(root + '/temp/' + foldertype + '.fakeextension', 'w+')
    for file in filelist:
        newfile.write(file)
