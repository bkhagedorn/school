import java.util.*;
public class TempConverter{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter temperature (in Fahrenheit)");
        double tempF = scan.nextDouble();
        double tempC = (tempF - 32) * (5.0/9.0);
        System.out.print("The temperature in Celsius is " + tempC + " C.");
    }
}
