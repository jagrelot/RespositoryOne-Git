# coding=utf-8
#Copyright © 2018 Acumen Solutions, Inc. The Thorax Salesforce Metadata Utility was
#created by Acumen Solutions. Except for the limited rights to use and make copies
#of the Software as provided in a License Agreement, all rights are reserved.


import os
import shutil
import sys
root = sys.argv[1]

flownames = os.listdir(root + '/temp/FlowDefinitions/flowDefinitions')

flowlist = []
try:
    with open(root + '/temp/Flow.flow') as flowfile:
        for line in flowfile:
            flowlist.append(line)

    for flowname in flownames:
        with open(root + '/temp/FlowDefinitions/flowDefinitions/' + flowname) as flowdefinition:
            for line in flowdefinition:
                if 'activeVersionNumber' in line:
                    flowtitle = flowname.split('.')[0]
                    activeVersion = line.strip()
                    activeVersion = activeVersion.replace('<activeVersionNumber>', '')
                    activeVersion = activeVersion.replace('</activeVersionNumber>', '')

                    for (i, flow) in enumerate(flowlist):
                        if flow == 'FileName: flows/' + flowtitle + '.flow\n':
                            flowlist[i] = 'FileName: flows/' + flowtitle + '-' + activeVersion + '.flow\n'

    with open(root + '/temp/Flow.flow', 'w+') as newflowfile:
        for line in flowlist:
            newflowfile.write(line)

    shutil.rmtree(root + '/temp/FlowDefinitions', ignore_errors=True)

except:
    print('No flows found')
