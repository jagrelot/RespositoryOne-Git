public with sharing class FlowFinishLocation {

     public Flow.Interview.New_Application_Flow  newApplicationFlow { get; set; }
  
     public String getAppID()
     {   
        if(newApplicationFlow == null)
           return '';
        else
           return newApplicationFlow.varApplicationID;
     }
     
     public PageReference getAppPage()
     {
        String finishLocation = '';
         if(getAppID() == null)
             finishLocation = newApplicationFlow.varAcct;
         else
             finishLocation = getAppID(); 
                       
         PageReference page = new PageReference('/'+ finishLocation);
         page.setRedirect(true);
         return page;
     }
        
}




/*
Public class FlowRedirectController{
  Public Flow.Interview.RedirectFlow redirectTo {get; set;}

  public FlowRedirectController() {
      Map<String, Object> forTestingPurposes = new Map<String, Object>();
      forTestingPurposes.put('vFinishLocation','codefriar.wordpress.com/');
      redirectTo = new Flow.Interview.RedirectFlow(forTestingPurposes);
  }

  Public PageReference getFinishLocation(){
      String finishLocation;
    if(redirectTo != null) {
      finishLocation = (string) redirectTo.getVariableValue('vFinishLocation');
    }
    PageReference send = new PageReference('/' + finishLocation);
    send.setRedirect(true);
    return send;
  }
}



*/