public class CardHand{
    private Card card1, card2;
    public CardHand(){
        card1 = new Card();
        card2 = new Card();
    }
    
    public boolean isMatch(){
        return card1.value() == card2.value();
    }
    
    public String toString(){
        return "Card 1: " + card1.value() + "\nCard 2: " + card2.value();
    }
}