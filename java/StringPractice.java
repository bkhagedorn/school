import java.util.Scanner;

public class StringPractice
{
    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter school and mascot");
        String input = scan.nextLine();
        
        if (input.contains("School"))
        {
            int sDex = input.indexOf("School");
            String school = input.substring(0, sDex + 6);
            String mascot = input.substring(sDex + 6);
            
            System.out.println("School name: " + school);
            System.out.print("Mascot name: " + mascot);
        }
        else
        {
            System.out.print("Invalid input");
        }
    }
}
