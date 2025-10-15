import java.util.*;

public class SumOfEvens
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter an integer value above or equal to 2");
        int x = scan.nextInt();
        int y = 0;
        
        if (x >= 2){
            for (int i = 2; i <= x; i += 2){
                if (i % 2 == 0)
                    y += i;
            }
            
            System.out.println();
            System.out.print(y);
        }
        else{
            System.out.println();
            System.out.print("Value is less than 2");
        }
    }
}
