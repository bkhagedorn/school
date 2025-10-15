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
        int input = scan.nextInt();
        for (int i = Integer.toString(input).length() - 1 ; i >= 0; i--){
            num = (input - (input % (int)Math.pow(10, i))) / (int)Math.pow(10, i);
            input = (input % (int)Math.pow(10, i));
            if (num % 2 == 0)
                evens++;
            else if (num % 2 != 0)
                odds++;
            else
                zeros++;
        }
        System.out.print(evens + " even numbers, " + odds + " odd numbers, and " + zeros + " zeros.");
    }
}
