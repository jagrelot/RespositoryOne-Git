# coding=utf-8
#Copyright © 2018 Acumen Solutions, Inc. The Thorax Salesforce Metadata Utility was
#created by Acumen Solutions. Except for the limited rights to use and make copies
#of the Software as provided in a License Agreement, all rights are reserved.

import sys
root = sys.argv[1]

standardValueSets = ['AccountContactMultiRoles',
                     'AccountContactRole',
                     'AccountOwnership',
                     'AccountRating',
                     'AccountType',
                     'AssetStatus',
                     'CampaignMemberStatus',
                     'CampaignStatus',
                     'CampaignType',
                     'CaseContactRole',
                     'CaseOrigin',
                     'CasePriority',
                     'CaseReason',
                     'CaseStatus',
                     'CaseType',
                     'ContactRole',
                     'ContractContactRole',
                     'ContractStatus',
                     'EntitlementType',
                     'EventSubject',
                     'EventType',
                     'FiscalYearPeriodName',
                     'FiscalYearPeriodPrefix',
                     'FiscalYearQuarterName',
                     'FiscalYearQuarterPrefix',
                     'IdeaMultiCategory',
                     'IdeaStatus',
                     'IdeaThemeStatus',
                     'Industry',
                     'LeadSource',
                     'LeadStatus',
                     'OpportunityCompetitor',
                     'OpportunityStage',
                     'OpportunityType',
                     'OrderType',
                     'PartnerRole',
                     'Product2Family',
                     'QuickTextCategory',
                     'QuickTextChannel',
                     'QuoteStatus',
                     'RoleInTerritory2',
                     'SalesTeamRole',
                     'Salutation',
                     'ServiceContractApprovalStatus',
                     'SocialPostClassification',
                     'SocialPostEngagementLevel',
                     'SocialPostReviewedStatus',
                     'SolutionStatus',
                     'TaskPriority',
                     'TaskStatus',
                     'TaskSubject',
                     'TaskType',
                     'WorkOrderLineItemStatus',
                     'WorkOrderPriority',
                     'WorkOrderStatus']

with open(root + '/temp/StandardValueSet.standardValueSet', 'w+') as file:
    for value in standardValueSets:
        file.write('FileName: standardvalueset/' + value + '.standardValueSet\n')
