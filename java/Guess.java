import java.util.*;

public class Guess
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String a, b, c;
        int x, y, z;
        
        System.out.print("Player 1, enter a word.");
        String input1 = scan.nextLine();
        System.out.print("Player 2, enter a word.");
        String input2 = scan.nextLine();
        
        x = input2.substring(0, 1).compareTo(input1.substring(0, 1));
        y = input2.substring(1, 2).compareTo(input1.substring(1, 2));
        z = input2.substring(2).compareTo(input1.substring(2));
        
        if (x > 0)
            a = "after";
        else if (x < 0)
            a = "before";
        else
            a = input2.substring(0, 1);
            
        if (y > 0)
            b = "after";
        else if (y < 0)
            b = "before";
        else
            b = input2.substring(1, 2);
            
        if (z > 0)
            c = "after";
        else if (z < 0)
            c = "before";
        else
            c = input2.substring(2);
        
        System.out.println();
        System.out.print(a + " " + b + " " + c);
    }
}
