import os
import shutil
import sys
root = sys.argv[1]

reportTypes = []
managedReportTypes = {}
webLinks = []
managedWebLinks = {}
translations = []

try:
    reportTypes = os.listdir(root + '/src/reportTypes')
    for reportType in reportTypes:
        if '__' in reportType:
            FullName = reportType.split('.')[0]
            BaseName = FullName.split('__')[1]
            Prefix = FullName.split('__')[0] + '__'
            managedReportTypes[BaseName] = FullName

except:
    print('No managed report types found')

try:
    webLinks = os.listdir(root + '/src/weblinks')
    for webLink in webLinks:
        if '__' in webLink:
            FullName = webLink.split('.')[0]
            BaseName = FullName.split('__')[1]
            Prefix = FullName.split('__')[0] + '__'
            managedWebLinks[BaseName] = FullName
            
except:
    print('No managed web links found')

try:
    translations = os.listdir(root + '/src/translations')

except:
    print('No translations found')

for translation in translations:
    lines = []
    with open(root + '/src/translations/' + translation, encoding="utf8") as file:
        lines = file.readlines()

    lineNum = -1
    line_iter = iter(lines)
    for line in line_iter:
        lineNum += 1
        if "<reportTypes>" in line:
            desc = 0
            if '<description>' in next(line_iter, None):
                next(line_iter, None)
                desc = 1
            nameLine = next(line_iter, None)
            name = nameLine.split('<name>')[1]
            name = name.split('</name>')[0]
            lineNum += 2 + desc
            if name in managedReportTypes:
                lines[lineNum] = lines[lineNum].replace(name, managedReportTypes[name])
                
        if "<customPageWebLinks>" in line:
            desc = 0
            next(line_iter, None)
            nameLine = next(line_iter, None)
            name = nameLine.split('<name>')[1]
            name = name.split('</name>')[0]
            lineNum += 2
            if name in managedWebLinks:
                lines[lineNum] = lines[lineNum].replace(name, managedWebLinks[name])

    with open(root + '/src/translations/' + translation, 'w+', encoding="utf8",) as file:
        for line in lines:
            file.write(line)
