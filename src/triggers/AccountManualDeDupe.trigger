trigger AccountManualDeDupe on Account (after insert) {

	List<Case> csList = new List<Case>();

	for (Account acct : Trigger.new) {
		
		Case cs      =  new Case();
		cs.OwnerId   = '005f4000000ML43';
		cs.Subject   = 'Dedupe this account';
		cs.AccountId = acct.Id;
		csList.add(cs);
	}

	insert csList;
}