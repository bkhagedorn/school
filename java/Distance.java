import java.util.*;

public class Distance
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the first X and Y coordinates");
        int x1 = scan.nextInt();
        int y1 = scan.nextInt();
        
        System.out.print("Enter the second X and Y coordinates");
        int x2 = scan.nextInt();
        int y2 = scan.nextInt();
        
        System.out.println();
        
        System.out.print("The distance is ");
        System.out.format("%.2f", Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((x2 - x1), 2)));
        System.out.print(" units.");
    }
}
