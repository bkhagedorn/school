import java.util.*;

public class P120
{
    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter number of seconds");
        int num = scan.nextInt();
    
        int hrs = num / 3600;
        num %= 3600;
        
        int mins = num / 60;
        num %= 60;
        
        System.out.println("Hours: " + hrs);
        System.out.println("Minutes: " + mins);
        System.out.print("Seconds: "+ num);
    }
}
