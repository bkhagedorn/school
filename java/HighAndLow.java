import java.util.*;

public class HighAndLow
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        boolean play = true;
        int num, input, guesses;
        while (play == true){
            guesses = 0;
            input = 0;
            num = rand.nextInt(100) + 1;
            System.out.print("Enter a number (1-100)");
            while (input != num){
                input = scan.nextInt();
                guesses++;
                if (input > num)
                    System.out.print("Higher");
                else if (input < num)
                    System.out.print("Lower");
            }
            System.out.println("You got it in " + guesses + " guesses.");
            System.out.print("Do you want to play again? (true/false)");
            play = scan.nextBoolean();
        }
    }
}
