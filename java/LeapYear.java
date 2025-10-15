import java.util.*;

public class LeapYear
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a year");
        int year = scan.nextInt();
        boolean leap = false;
        
        if (year % 4 == 0)
            if (year % 100 == 0)
                if (year % 400 == 0)
                    leap = true;
                else
                    ;
            else
                leap = true;
        
        if (leap)
            System.out.print(year + " is a leap year.");
        else
            System.out.print(year + " is not a leap year.");
    }
}
