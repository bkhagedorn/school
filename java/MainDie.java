public class MainDie{
    public static void main(String[] args) {
        Die die1 = new Die();
        Die die2 = new Die(12);
        
        int value = die1.getFaceValue();
        int value2 = die2.getFaceValue(); 
        System.out.println(value);
        System.out.println(value2);
        
        die1.roll();
        die2.roll();
        Die.message();
        
        value = die1.getFaceValue();
        value2 = die2.getFaceValue(); 
        System.out.println(value);
        System.out.println(value2);
    }
}