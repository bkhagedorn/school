import java.util.*;

public class Backwards
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Enter a capitalized word");
        String input = scan.nextLine();
        char cap = input.charAt(input.length()-1);
        
        System.out.println();
        
        String word = input.toLowerCase();
        String word2 = word.replace(input.charAt(input.length()-1), Character.toUpperCase(cap));
        
        System.out.print(word2);
    }
}
