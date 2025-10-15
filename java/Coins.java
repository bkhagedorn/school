import java.util.Scanner;

public class Coins
{
    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter number of pennies");
        int p = scan.nextInt();
        
        System.out.println("Enter number of nickels");
        int n = scan.nextInt();
        
        System.out.println("Enter number of dimes");
        int d = scan.nextInt();
        
        System.out.println("Enter number of quarters");
        int q = scan.nextInt();
        
        System.out.println();
        
        double total = (0.01 * p) + (0.05 * n) + (0.1 * d) + (0.25 * q);
        System.out.print("The total is $");
        System.out.format("%.2f", total);
    }
}
