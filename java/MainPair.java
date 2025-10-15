public class MainPair{
    public static void main(String[] args) {
        PairOfDice myDice = new PairOfDice();
        int total;
        int count = 0;
        
        for (int i = 0; i < 1000; i++){
            total = myDice.roll();
            System.out.println(total);
            if (total == 12)
                count++;
        }
        System.out.println("Boxcars: " + count);
    }
}
