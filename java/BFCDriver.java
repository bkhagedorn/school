public class BFCDriver
{
    public static void main(String[] args) {
       System.out.println ("Welcome to the BFC.\n");


     BFC bank = new BFC();


     bank.createAccount();
     bank.deposit();
     System.out.println ("Current Status:");
     System.out.println (bank);


     bank.createAccount();
     bank.deposit();
     System.out.println ("Current Status:");
     System.out.println (bank);


     bank.createAccount();
     bank.deposit();
     System.out.println ("Current Status:");
     System.out.println (bank);


     bank.withdraw();
     System.out.println ("Current Status:");
     System.out.println (bank);


     bank.withdraw();
     System.out.println ("Current Status:");
     System.out.println (bank);


     bank.interest();
     System.out.println ("Current Status:");
     System.out.println (bank);

    }
}
