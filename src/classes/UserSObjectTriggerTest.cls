@isTest(seeAlldata=true)
private class UserSObjectTriggerTest {

	@isTest static void createUser() {
		Profile profile = [SELECT Id FROM Profile WHERE Name='System Administrator'];
		User sfuser = new User();
		sfuser.ProfileId  = profile.id;
		sfuser.firstName = 'Test';
		sfuser.lastName  = 'User';
		sfuser.alias     = 'Tuse';
		sfuser.Email     = 'Tuser@mailing.com';
		sfuser.Username  = 'Tuser@mailing.com';
		sfuser.CommunityNickname  = 'TuseTrigger';
		sfuser.TimeZoneSidKey = 'America/Los_Angeles';
		sfuser.LocaleSidKey   = 'en_US';
		sfuser.LanguageLocaleKey = 'en_US';
		sfuser.EmailEncodingKey  = 'ISO-8859-1';
		insert sfuser;
     }	
  }