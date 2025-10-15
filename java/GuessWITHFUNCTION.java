import java.util.*;

public class GuessWITHFUNCTION
{
    private static int getCompare(int index1, int index2, String input1, String input2)
    {
        return input2.substring(index1, index2).compareTo(input1.substring(index1, index2));
    }
    
    private static String beforeAfter(int index, String input1, int num)
    {
        if (index > 0)
            return "after";
        else if (index < 0)
            return "before";
        else
            return input1.substring(num, num + 1).toUpperCase();
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int x, y, z;
        String a, b, c;
        
        System.out.print("Player 1, enter a word.");
        String input1 = scan.nextLine();
        System.out.print("Player 2, enter a word.");
        String input2 = scan.nextLine();
        
        x = getCompare(0, 1, input1, input2);
        y = getCompare(1, 2, input1, input2);
        z = getCompare(2, 2, input1, input2);
        
        a = beforeAfter(x, input1, 0);
        b = beforeAfter(y, input1, 1);
        c = beforeAfter(z, input1, 2);
        
        System.out.println();
        System.out.print(a + " " + b + " " + c);
    }
}
