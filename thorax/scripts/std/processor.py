#Copyright © 2018 Acumen Solutions, Inc. The Thorax Salesforce Metadata Utility was
#created by Acumen Solutions. Except for the limited rights to use and make copies
#of the Software as provided in a License Agreement, all rights are reserved.

def processStandard(componentfile, suffix):

    componentlist = []
    
    for line in componentfile:
        if 'FileName: ' in line:
            componentname = processComponentName(line, suffix)

            #skips managed classes
            #if suffix == 'cls' and '__' in componentname:
            #    continue
            
            componentlist.append(componentname)
                        
    return componentlist;

def processLayouts(componentfile, suffix):

    componentlist = []

    counter = 0
    prefix = '-null__'
    componentname = 'null'
    for line in componentfile:
        if counter == 1:
            componentname = processComponentName(line, suffix)
            counter += 1
        elif counter == 4:
            prefix = processPrefix(line)
            if prefix == '-null__':
                componentlist.append(componentname)
                componentname = 'null'
                counter +=1
            else:
                half1 = componentname.split('-', 1)[0]
                half2 = componentname.split('-', 1)[1]
                componentname = half1 + prefix + half2
                componentlist.append(componentname)
                componentname = 'null'
                counter +=1
        elif counter == 7:
            counter = 0
        else:
            counter +=1

    return componentlist;

def processComponentName(line, suffix):
    try:
        componentname = line.split('/', 1)[1]
        componentname = componentname.replace('.' + suffix, '')
        componentname = componentname.replace('\n', '')
    except:
        componentname = '*'
    
    return componentname;

def processPrefix(line):
    prefix = line.replace('Namespace Prefix: ', '')
    prefix = prefix.replace('\n', '')
    prefix = '-' + prefix + '__'
    return prefix;
