trigger UserSObjectTrigger on User (before insert) {

List<Contact> contactListToUpdate = new List<Contact>();
List<Account> assignedAccount = [
	SELECT Id, Name
	FROM Account
	WHERE Name='Internal Account'
	LIMIT 1];
	
	for (User sfuser : Trigger.new) {
			Contact sfcontact = new Contact();
			sfcontact.firstName = sfuser.firstName;
			sfcontact.lastName  = sfuser.lastName;
			sfcontact.AccountId = assignedAccount.get(0).Id;
			contactListToUpdate.add(sfcontact);
		}	

		insert contactListToUpdate;
}