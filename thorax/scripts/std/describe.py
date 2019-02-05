# coding=utf-8
#Copyright © 2018 Acumen Solutions, Inc. The Thorax Salesforce Metadata Utility was
#created by Acumen Solutions. Except for the limited rights to use and make copies
#of the Software as provided in a License Agreement, all rights are reserved.

import os
import sys
root = sys.argv[1]

with open(root + '/describe.txt') as raw:
    block = ''
    metadataTypes = []
    for line in raw:
        if 'ChildObjects' in line:
            block += line
            metadataTypes.append(block)
            block = ''
        else:
            block += line

    with open(root + '/standardTypes.csv', 'w+') as newfile:
        finallines = []
        for chunk in metadataTypes:
            xmlname = ''
            suffix = ''
            infolder = False
            lines = chunk.split('\n')
            for line in lines:
                if 'XMLName' in line:
                    xmlname = line.replace('XMLName: ', '')
                elif 'Suffix' in line:
                    suffix = line.replace('Suffix: ', '')
                elif 'InFolder: true' in line:
                    infolder = True
            if infolder == True:
                continue
            finalline = xmlname + ',' + suffix
            finallines.append(finalline)
        finallines = sorted(finallines)
        for line in finallines:
            newfile.write(line + '\n')

os.remove(root + '/describe.txt')
