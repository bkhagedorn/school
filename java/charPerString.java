import java.util.*;
public class charPerString{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = scan.nextLine();
        System.out.println();
        for (int i = 0; i < str.length(); i++){
            if (i != str.length() - 1)
                System.out.println(str.charAt(i));
            else
                System.out.print(str.charAt(i));
        }
    }
}
