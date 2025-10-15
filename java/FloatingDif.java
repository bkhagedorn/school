import java.util.*;
public class FloatingDif{
    public static void main (String[] arg)
    {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter 2 doubles");
        double num1 = scan.nextDouble();
        double num2 = scan.nextDouble();
        System.out.println("The sum is " + (num1 + num2));
        System.out.println("The difference is " + (Math.abs(num1 - num2)));
        System.out.print("The product is " + (num1 * num2));
    }
}