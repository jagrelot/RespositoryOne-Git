# coding=utf-8
#Copyright © 2018 Acumen Solutions, Inc. The Thorax Salesforce Metadata Utility was
#created by Acumen Solutions. Except for the limited rights to use and make copies
#of the Software as provided in a License Agreement, all rights are reserved.

import os
import shutil
import sys
root = sys.argv[1]

deploymentFlows = []
flowDefinitions = []

try:
    deploymentFlows = os.listdir(root + '/deploy/flows')
    flowDefinitions = os.listdir(root + '/temp/FlowDefinitions/flowDefinitions')
except:
    print('No flows in this deployment')
    sys.exit(0)

activeFlowNames = []

try:
    for flowDefinitionName in flowDefinitions:
        with open(root + '/temp/FlowDefinitions/flowDefinitions/' + flowDefinitionName) as flowDefinition:
            for line in flowDefinition:
                if 'activeVersionNumber' in line:
                    flowTitle = flowDefinitionName.split('.')[0]
                    activeVersion = line.strip()
                    activeVersion = activeVersion.replace('<activeVersionNumber>', '')
                    activeVersion = activeVersion.replace('</activeVersionNumber>', '')

                    activeFlowName = flowTitle + '-' + activeVersion + '.flow'
                    activeFlowNames.append(activeFlowName)

    for deploymentFlow in deploymentFlows:
        if deploymentFlow in activeFlowNames:
            os.remove(root + '/deploy/flows/' + deploymentFlow)

    shutil.rmtree(root + '/temp')

except Exception as e:
    print(e)
    sys.exit(1)
