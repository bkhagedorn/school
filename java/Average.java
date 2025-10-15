import java.util.*;
public class Average
{
    public static void main (String[] arg)
    {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter 3 numbers");
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        int num3 = scan.nextInt();
        System.out.print("The average is " + (num1 + num2 + num3)/3);
    }
}