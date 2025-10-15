import java.util.*;

public class VowelCounter
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a word");
        String x = scan.nextLine().toLowerCase();
        int b = 0, c = 0, d = 0;
        int a = 0, e = 0, i = 0, o = 0, u =0;
        
        for (int it = 0; it < x.length(); it++){
            if (x.codePointAt(it) == 97)
                a++;
            else if (x.codePointAt(it) == 101)
                e++;
            else if (x.codePointAt(it) == 105)
                i++;
            else if (x.codePointAt(it) == 111)
                o++;
            else if (x.codePointAt(it) == 117)
                u++;
            else if (x.codePointAt(it) == 32)
                b++;
            else if (x.codePointAt(it) == 33 || x.codePointAt(it) == 46 || x.codePointAt(it) == 63)
                c++;
            else
                d++;
        }
        System.out.println();
        System.out.println("A: " + a + ", E: " + e + ", I: " + i + ", O: " + o + ", U: " + u);
        System.out.print(b + " spaces, " + c + " punctuation marks, and " + d + " consonants.");
    }
}