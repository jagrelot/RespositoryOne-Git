public class SOQLController {
    public String name {get;set;}
    public List<Contact> queryResult {get;set;}

     public PageReference query(){
        String qryString = 'SELECT Id FROM Contact WHERE ' + 
        '(IsDeleted = false and Name like \'%' + name + '%\')';
        queryResult = Database.query(qryString);
        return null;
    }
}