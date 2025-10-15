public class MainCardHand
{
    public static void main(String[] args) {
        CardHand cardhand;
        for (int i = 0; i < 10; i++){
            cardhand = new CardHand();
            System.out.println(cardhand);
            System.out.println(cardhand.isMatch());
            System.out.println();
        }
    }
}