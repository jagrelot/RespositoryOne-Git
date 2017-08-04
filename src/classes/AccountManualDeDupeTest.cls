@isTest
private class AccountManualDeDupeTest {
	
	@isTest static void createAcccount() {
		
		Account acct = new Account();
		acct.name    = 'Test Business Account';
		insert acct;
	}
	
}