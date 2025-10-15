import java.util.*;

public class LowestTemp {
  public static void main(String args[]) {
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter 7 temperatures");
    double[] temps = new double[7];
    int test = 0;
    int test2 = 1;
    for (int i = 0; i < 7; i++){
        temps[i] = scan.nextDouble();
    }
    
    double lowestTemp = temps[0];
    
    for (double i : temps){
        test++;
        if (i < lowestTemp){
            lowestTemp = i;
            test2 = test;
        }
    }
    
    System.out.println("\nThe lowest temperature was " + lowestTemp + " on Day " + test2);
  }
}