public class PairOfDice{
    private Die die1, die2;
    
    public PairOfDice(){
        die1 = new Die();
        die2 = new Die(); 
    }
    
    public int roll(){
        return die1.roll() + die2.roll();
    }
    
    public String toString(){
        return "die1 = " + die1 + "\ndie2 = " + die2;
    }
}