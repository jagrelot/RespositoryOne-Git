trigger LeadingCompetitor on Lead (before insert, before update) {

	for (Lead loopLead : Trigger.new) {
       
		//Add all our prices in a list in order of competitor
		List<Decimal> prices = new List<Decimal>();
		prices.add(loopLead.Competitor_1_Price__c);
		prices.add(loopLead.Competitor_2_Price__c);
		prices.add(loopLead.Competitor_3_Price__c);

	   //Add all our competitors in a list in order

	    List<String> competitors = new List<String>();
	    competitors.add(loopLead.Competitor_1__c);
	    competitors.add(loopLead.Competitor_2__c);
	    competitors.add(loopLead.Competitor_3__c);

       //Loop through all competitors to find the position of the lowest price

	   Decimal highestPrice;
	   Integer highestPricePosition;

	    for(Integer i = 0; i < prices.size(); i++){
	    	Decimal currentPrice = prices.get(i);
	    	if(highestPrice == null || currentPrice > highestPrice){
	    		highestPrice = currentPrice;
	    		highestPricePosition = i;
	    	}
	    }

	   //Populates the leading competitor field with the competitor matching the lowest position.
	   loopLead.LeadingCompetitor__c = competitors.get(highestPricePosition);
	   loopLead.Price__c = prices.get(highestPricePosition);
   }
}



//1. Populate the most expensive competitor instead
//2. Populate the competior price too

/*
	Put all our prices in a list so we can loop through it
	(Our prices should be added in order from competitor 1 - 3)
	Loop through all of our prices and find the lowest one
	Note the list position of out lowest price

	Put all our competitors in a list
	(Out competitors shoul be added in order from  competitor 1-3)
	Use the competitor with the same postion as our lowest price

	=====This finds the highest price of the competitors using if statements====	

		if (loopLead.Competitor_1_Price__c >= loopLead.Competitor_2_Price__c && loopLead.Competitor_1_Price__c >= loopLead.Competitor_3_Price__c){
            loopLead.LeadingCompetitor__c = loopLead.Competitor_1__c;

		}else if(loopLead.Competitor_2_Price__c >= loopLead.Competitor_1_Price__c && loopLead.Competitor_2_Price__c >= loopLead.Competitor_3_Price__c){
			loopLead.LeadingCompetitor__c = loopLead.Competitor_2__c;

		}else if(loopLead.Competitor_3_Price__c >= loopLead.Competitor_1_Price__c && loopLead.Competitor_3_Price__c >= loopLead.Competitor_2_Price__c){
			loopLead.LeadingCompetitor__c = loopLead.Competitor_3__c;

		}
	} 
	*/