trigger AssignLeadGrade on Lead (before insert, before update) {

	for (Lead loopLead : Trigger.new) {
		if(loopLead.Score__c != null){
			if(loopLead.Score__c  == 100){
				loopLead.Grade__c = 'A+';
			} else if (loopLead.Score__c >= 90){
				loopLead.Grade__c = 'A';
			} else if (loopLead.Score__c >= 80){
	            loopLead.Grade__c = 'B';
			} else{
				loopLead.Grade__c = 'F';
				loopLead.Status   = 'Closed - Trash';
			}			
		}
	}
}

/*
	Null Pointer Exception
	+The most common coding error of all time.
    +Often happen when using dot notation.


    Always user DML!
    ..except on Trigger.new recrods in before triggers

*/