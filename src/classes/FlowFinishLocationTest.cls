@isTest
private class FlowFinishLocationTest {
	
  static testmethod void testFinishLocationMethod(){
		PageReference pageRef = Page.NewApplicationFlowPage;
		Test.setCurrentPage(pageRef);
		FlowFinishLocation testCtrl = new FlowFinishLocation();
		System.assertEquals(testCtrl.getAppPage().getUrl(), ' ');
    
	}
}


/*
 Account acct = new Account();
    	  acct.Name = 'Test Account';
    	  insert acct;

    	  Test.startTest();
          Flow.Interview.New_Application_Flow newApplicationFlowTest;
          newApplicationFlowTest.varAcct     = acct.id;
          newApplicationFlowTest.varAcctName = acct.Name;


          testCtrl.getFinishLocation().getUrl(), '/codefriar.wordpress.com/');
*/