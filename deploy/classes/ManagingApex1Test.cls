@isTest
public class ManagingApex1Test {

	public static final Integer accountCount = 2;
	public static final Integer contactsOnEachAccount = 3;

	@testsetup
	public static void initializeClassTestData(){
		CreateTestAccounts(accountCount,contactsOnEachAccount);
	}
	
	 public static void CreateTestAccounts(Integer accounts, Integer contactsPerAccount) {

	 	Database.DMLOptions dml = new Database.DMLOptions();
	 	dml.DuplicateRuleHeader.allowSave = true;
		
		List<Account> accountList = new List<Account>();
		for(Integer a = 0; a < accounts; a++){

			accountList.add(new Account(Name='Jose\'s Company' + String.valueOf(a)));

		}

		database.insert(accountList,dml);

		List<Contact> contacts = new List<Contact>();

		for(Account act : accountList){

			for(Integer c = 0 ; c < contactsPerAccount; c++){

				contacts.add(new Contact(FirstName = 'Jose' , LastName = 'Agrelot' + String.valueOf(c), AccountID = act.id ));
			}
		}

		database.insert(contacts, dml);

	}

	public static User getTestUser() {

	 User u = new User(
     ProfileId = UserInfo.getProfileId(),
     LastName = 'Agrelot',
     Email = 'jagrelot000@amamama.com',
     Username = 'jagrelot000@amamama.com',
     TimeZoneSidKey = 'America/Los_Angeles',
     EmailEncodingKey = 'UTF-8',
     LanguageLocaleKey = 'en_US',
     LocaleSidKey = 'en_US');

	 return u;
	}
	
}