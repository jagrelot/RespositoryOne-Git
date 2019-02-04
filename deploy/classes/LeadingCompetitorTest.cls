@isTest
private class LeadingCompetitorTest {
	
	@isTest static void test_method_one() {
		// Create an opportunity and set required fields
		Opportunity opp = new Opportunity();
		opp.Name        = 'Big Deal';
		opp.CloseDate   = Date.today();
		opp.StageName   = 'Prospecting';
	}
	
	
}


/*
	1.Create or Update an opportunity
	2.Populate all 3 competitor price fields
	3.Populate all 3 competitor fiels

*/