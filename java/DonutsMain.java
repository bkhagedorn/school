import java.util.*;

public class DonutsMain
{
    public static void main(String[] args) {
        int a, b, c;
        Scanner scan = new Scanner(System.in);
        
        System.out.print("How many glazed?");
        a = scan.nextInt();
        
        System.out.print("How many long johns?");
        b = scan.nextInt();
        
        System.out.print("How many cream filled?");
        c = scan.nextInt();
        
        Donuts order = new Donuts(a, b, c);
        
        System.out.println();
        System.out.println("Order");
        System.out.println(order.toString());
        System.out.println();
        System.out.println("Cost");
        System.out.print("$" + Double.toString(order.cost()));
    }
}