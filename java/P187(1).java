import java.util.*;

public class P187
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int odds = 0;
        int evens = 0;
        int zeros = 0;
        int num = 0;
        
        System.out.print("Enter a number");
        String input = scan.nextLine();
        for (int i = 0; i <= input.length() - 1; i++){
            num = Integer.parseInt(Character.toString(input.charAt(i)));
            if (num == 0)
                zeros++;
            else if (num % 2 == 0)
                evens++;
            else
                odds++;
        }
        System.out.print(evens + " even numbers, " + odds + " odd numbers, and " + zeros + " zeros.");
    }
}
