public with sharing class LoanCustomController {

    private final Loan__c loan;
    private final List<Loan__C> loans;
    private User  underwriter;
    private Boolean approved;

    public LoanCustomController() {
        loan = [SELECT Id, Amount__c, Approved__c, Borrower_First_Name__c, 
                       Borrower_Last_Name__c, Name, Underwriter__c, Risk_Level__c FROM Loan__c
                   WHERE Id = :ApexPages.currentPage().getParameters().get('id')];
                   
        underwriter = [SELECT Id, Name FROM User Where Id = :loan.Underwriter__c ];
        
        loans = [SELECT Id, Amount__c, Approved__c, Borrower_First_Name__c, 
                       Borrower_Last_Name__c, Name, Underwriter__c, Risk_Level__c FROM Loan__c];
               
    }
    
    public String getLoanName() {
        return loan.Name;
    }

     public String getName() {
        return loan.Borrower_First_Name__c + ' ' + loan.Borrower_Last_Name__c;
    }
    
     public Decimal getAmount() {
        return loan.Amount__c;
    }
   
     public Boolean getApproved() {
        return loan.Approved__c;
    }
 
     public String getUnderwriter() {
       return underwriter.name;
    }
    
     public String getRiskLevel() {
        return loan.Risk_Level__c;
    }
    
     public Boolean getApprovedIndirectRef() {
        approved = loan.Approved__c;
        return approved;
    }

     public List<Loan__c> getLoansList() {
        return loans;
    }

}