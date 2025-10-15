import java.util.*;

public class RandomString
{
    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        
        System.out.print("Enter a string.");
        String input = scan.nextLine();
        
        int index = rand.nextInt(input.length());

        System.out.print("The part of your string from the index " + index + " to the end is: " + input.substring(index));
        
    }
}
