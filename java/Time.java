import java.util.*;

public class Time
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Enter hours");
        int hrs = scan.nextInt();
        
        System.out.print("Enter minutes");
        int mins = scan.nextInt();
        
        System.out.print("Enter seconds");
        int secs = scan.nextInt();
        
        System.out.println();
        
        System.out.print("The total amount of seconds is " + ((hrs * 3600) + (mins * 60) + secs));
    }
}