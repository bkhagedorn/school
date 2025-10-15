public class BasketballGame{
    private int onePointers, twoPointers, threePointers, onesAttempted, twosAttempted, threesAttempted;
    public BasketballGame(int a, int b, int c, int d, int e, int f){
        onePointers = a;
        twoPointers = b;
        threePointers = c;
        onesAttempted = d;
        twosAttempted = e;
        threesAttempted = f;
    }
    
    public int score(){
        return onePointers + (twoPointers * 2) + (threePointers * 3);
    }
    
    public double percentage(String type){
        if (type.toLowerCase().equals("one"))
            return (double)onePointers/onesAttempted * 100;
        else if (type.toLowerCase().equals("two"))
            return (double)twoPointers/twosAttempted * 100;
        else if (type.toLowerCase().equals("three"))
            return (double)threePointers/threesAttempted * 100;
        return 0.0;
    }
    
    public static void message(){
        System.out.print("Welcome to March Madness!");
    }
}