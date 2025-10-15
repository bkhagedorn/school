import java.util.*;

public class MoreStringPractice
{
    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Enter your first and last name");
        String name = scan.nextLine();
        
        int space = name.indexOf(" ");
        
        String FName = name.substring(0, space);
        String LName = name.substring(space + 1);
        
        char FLetter = FName.charAt(0);
        char LLetter = LName.charAt(0);
        
        System.out.println();
        
        System.out.println(LName + ", " + FName);
        System.out.println(FName.toUpperCase() + " " + LName.toUpperCase());
        System.out.print(FLetter + "" + LLetter);
    }
}
