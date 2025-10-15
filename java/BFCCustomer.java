public class BFCCustomer{
    private int userID;
    private String name;
    private double balance;
    public BFCCustomer(int a, String b, double c){
        userID = a;
        name = b;
        balance = c;
    }
    
    public int getUserID(){
        return userID;
    }
    
    public String getName(){
        return name;
    }
    
    public double getBalance(){
        return balance;
    }
    
    public String toString(){
        return "UserID: " + userID + "\nName: " + name + "\nBalance: " + balance;
    }
    
    public void setBalance(double a){
        balance = a;
    }
}
