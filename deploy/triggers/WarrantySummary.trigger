trigger WarrantySummary on Case (before insert) {

    for(Case cs : Trigger.new){

        // Set up vvariables to use in the summary field
        String  purchasedDate       = cs.ProductPurchaseDate__c.format();
        String  createDate          = DateTime.now().format();
        Integer warrantyDays        = cs.ProductTotalWarrantyDays__c.intValue();
        Decimal warrantyPercentage  = 100 * ((cs.ProductPurchaseDate__c.daysBetween(Date.today()) / cs.ProductTotalWarrantyDays__c)).setScale(2);
        Boolean hasExtendedWarranty = cs.ProductHasExtendedWarranty__c; 
        
        //Populate summary field
        cs.WarrantySummary__c =    'Product purchased on ' + purchasedDate + ' '
                                 + 'and case created on' +  createDate + '\n'
                                 + 'days and is ' + warrantyPercentage + '% through its warranty period.\n'
                                 + 'Extended warranty: ' + hasExtendedWarranty + '\n'
                                 + 'Have a nice day!';
    }

}
/*
Product purchased on <<Purchased Date>> and case created on <<Case Created Date>>/
Warranty is for <<Warranty Total Days>> days and is <<Warranty Percentage>>% through its warranty period.
Extended warranty: <<Has Extended Warranty>>
Have a nice day!
*/