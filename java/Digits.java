import java.util.*;
public class Digits
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int odds = 0;
        int evens = 0;
        int zeros = 0;
        
        System.out.print("Enter an integer value");
        String str = scan.nextLine();
        char[] chars = new char[str.length()];

        for (int i = 0; i < str.length(); i++){
            chars[i] = str.charAt(i);
        }
        for (char i : chars){
            if (Integer.parseInt(String.valueOf(i)) == 0)
                zeros++;
            else if (Integer.parseInt(String.valueOf(i)) % 2 == 0)
                evens++;
            else
                odds++;
        }
        
        System.out.print("There are " + evens + " evens, " + odds + " odds, and " + zeros + " zeros.");
    }
}
