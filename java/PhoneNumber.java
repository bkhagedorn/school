import java.util.*;

public class PhoneNumber
{
    public static void main(String[] args) {
        Random rand = new Random();
        
        int digit1 = (rand.nextInt(7) + 1);
        int digit2 = rand.nextInt(8);
        int digit3 = rand.nextInt(8);
        
        int digits = rand.nextInt(643) + 100;
        int digits2 = rand.nextInt(9000) + 1000;
        
        System.out.print((digit1 + "" + digit2 + "" + digit3) + "-" + digits + "-" + digits2);
    }
}
