import java.util.Scanner;

public class SumWithInput
{
    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        int a;
        int b;
        
        System.out.print("Enter a number");
        a = scan.nextInt();
        
        System.out.print("Enter another number");
        b = scan.nextInt();
        
        System.out.println();
        System.out.print("The sum is " + (a + b));
    }
}
