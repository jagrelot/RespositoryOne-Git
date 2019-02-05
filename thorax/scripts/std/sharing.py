# coding=utf-8
#Copyright © 2018 Acumen Solutions, Inc. The Thorax Salesforce Metadata Utility was
#created by Acumen Solutions. Except for the limited rights to use and make copies
#of the Software as provided in a License Agreement, all rights are reserved.


import os
import shutil
import sys
root = sys.argv[1]

rulenames = []

try:
    rulenames = os.listdir(root + '/temp/SharingRules/sharingRules')

except:
    print('No sharing rules found')

for (i, rulename) in enumerate(rulenames):
    rulenames[i] = 'FileName: sharingRules/' + rulename + '\n'

    with open(root + '/temp/SharingRules.sharingRules', 'w+') as sharingrulelist:
        for row in rulenames:
            sharingrulelist.write(row)

    shutil.rmtree(root + '/temp/SharingRules', ignore_errors=True)


