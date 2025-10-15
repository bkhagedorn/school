import java.util.*;

public class BFC{
    Scanner scan = new Scanner(System.in);
    private BFCCustomer[] customerArray;
    private int count;
    public BFC(){
        customerArray = new BFCCustomer[30];
        count++;
    }
    
    public void createAccount(){
        System.out.print("Enter user ID and name:");
        int id = scan.nextInt();
        String srgh = scan.nextLine();
        String name = scan.nextLine();
        BFCCustomer account = new BFCCustomer(id, name, 0);
        customerArray[id] = account;
    }
    
    public BFCCustomer[] getCustomers(){
        return customerArray;
    }
    
    public String toString(){
        String str = "";
        for (int i = 0; i < customerArray.length; i++){
            if (customerArray[i] != null)
                str += customerArray[i].toString() + "\n\n";
        }
        return str;
    }
    
    public void deposit(){
        System.out.print("Enter UserID and amount");
        int id = scan.nextInt();
        double amount = scan.nextDouble();
        BFCCustomer customer = customerArray[id];
        customer.setBalance(customer.getBalance() + amount);
    }
    
    public void withdraw(){
        System.out.print("Enter UserID and amount");
        int id = scan.nextInt();
        double amount = scan.nextDouble();
        BFCCustomer customer = customerArray[id];
        customer.setBalance(customer.getBalance() - amount);
    }
    
    public int findUserID(){
        System.out.print("Enter UserID");
        int id = scan.nextInt();
        return id;
    }
    
    public void interest(){
        for (BFCCustomer i : customerArray){
            if (i != null)
                i.setBalance(i.getBalance() + (i.getBalance() * 0.03));
        }
    }
}