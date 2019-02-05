# coding=utf-8
#Copyright © 2018 Acumen Solutions, Inc. The Thorax Salesforce Metadata Utility was
#created by Acumen Solutions. Except for the limited rights to use and make copies
#of the Software as provided in a License Agreement, all rights are reserved.

import os
import sys
sys.path.append(os.getcwd() + '/scripts/std')
from writer import *
root = sys.argv[1]
version = float(sys.argv[2])

print('Thorax -- Building package.xml')
filenames = os.listdir(root + '/temp')

package = open(root + '/src/package.xml', 'w+')

writeHeader(package)

for filename in filenames:
    writeComponents(filename, package, root)

writeFooter(package, version)
