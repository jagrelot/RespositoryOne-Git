@isTest
private class WarrantySummaryTest {
	
	@isTest static void createCaseforWarranty() {
		
		Case cs = new Case();
		cs.ProductPurchaseDate__c          = Date.today();
		cs.ProductTotalWarrantyDays__c     = 10;
		cs.ProductHasExtendedWarranty__c   = true;

		insert cs;

	}
	
	
}