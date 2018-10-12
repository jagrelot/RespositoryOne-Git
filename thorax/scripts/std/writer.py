#Copyright © 2018 Acumen Solutions, Inc. The Thorax Salesforce Metadata Utility was
#created by Acumen Solutions. Except for the limited rights to use and make copies
#of the Software as provided in a License Agreement, all rights are reserved.

from processor import *

def writeHeader(package):
    package.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    package.write('<Package xmlns="http://soap.sforce.com/2006/04/metadata">\n')
    return;

def writeComponents(filename, package, root):

    package.write('    <types>\n')

    xmlname = filename.split('.')[0]
    suffix = filename.split('.')[1]
    
    with open(root + '/temp/' + filename) as componentfile:
    
        if xmlname == 'Layout':
            componentlist = processLayouts(componentfile, suffix)

        else:
            componentlist = processStandard(componentfile, suffix)

    componentlist = list(set(componentlist))
    componentlist = sorted(componentlist)

    for component in componentlist:
        package.write('        <members>' + component + '</members>\n')

    package.write('        <name>' + xmlname + '</name>\n')    
    package.write('    </types>\n')
    
    return;

def writeFooter(package, version):
    package.write('    <version>' + '{:03.1f}'.format(version) + '</version>\n')
    package.write('</Package>')
    return;
