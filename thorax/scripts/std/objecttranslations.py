# coding=utf-8
import os
import shutil
import sys
root = sys.argv[1]

layouts = []
managedLayouts = {}
translations = []

try:
    layouts = os.listdir(root + '/src/layouts')

except:
    print('No layouts found')

for layout in layouts:
    if '__' in layout.split('-', 1)[1]:
        fullName = layout.rsplit('.', 1)[0]
        objectName = fullName.split('-', 1)[0]
        layoutName = fullName.split('-', 1)[1]
        baseName = layoutName.split('__', 1)[1]
        prefix = layoutName.split('__', 1)[0] + '__'
        fullNameNoPrefix = objectName + '-' + baseName
        managedLayouts[fullNameNoPrefix] = {'fullName': fullName,
                                            'objectName': objectName,
                                            'layoutName': layoutName,
                                            'baseName': baseName,
                                            'prefix': prefix}

try:
    translations = os.listdir(root + '/src/objectTranslations')

except:
    print('No object translations found')

for translation in translations:
    lines = []
    objectName = translation.split('-', 1)[0]
    with open(root + '/src/objectTranslations/' + translation, encoding="utf8") as file:
        lines = file.readlines()

    for (i, line) in enumerate(lines):
        if "<layout>" in line and '</layout>' in line:
            name = line.split('<layout>')[1]
            name = name.split('</layout>')[0]
            fullNameNoPrefix = objectName + '-' + name
            if fullNameNoPrefix in managedLayouts:
                lines[i] = lines[i].replace(name, managedLayouts[fullNameNoPrefix]['layoutName'])

    with open(root + '/src/objectTranslations/' + translation, 'w+', encoding="utf8",) as file:
        for line in lines:
            file.write(line)
