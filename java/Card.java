import java.util.*;
public class Card{
    private int value;
    Random rand = new Random();
    public Card(){
        value = rand.nextInt(12)+1;
    }
    
    public void draw(){
        value = rand.nextInt(12)+1;
    }
    
    public int value(){
        return value;
    }
    
    public String toString(){
        return "Card: " + value;
    }
}