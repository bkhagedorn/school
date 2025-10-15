import java.util.*;
public class sumAbove2{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a value above 2:");
        int val = scan.nextInt();
        int sum = 0;
        if (val < 2)
            System.out.print("Value must be above or equal to 2");
        else{
            for (int i = 2; i < val; i++){
                sum += i;
            }
            System.out.print("The sum is " + sum + ".");
        }
    }
}
