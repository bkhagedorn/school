import java.util.*;

public class Beer
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number of bottles");
        int input = scan.nextInt();
        
        System.out.println();
        
        for (int x = input; x > 0; x--)
        {
            System.out.println(x + " bottles of beer on the wall");
            System.out.println(x + " bottles of beer");
            System.out.println("If one of those bottles should happen to fall");
            if (x > 1)
                System.out.println(x - 1 + " bottles of beer on the wall");
            else
                System.out.println("No more bottles of beer on the wall");
        }
    }
}