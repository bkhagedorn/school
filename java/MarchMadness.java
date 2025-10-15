public class MarchMadness
{
    public static void main(String[] args) {
        BasketballGame game = new BasketballGame(10, 20, 5, 15, 40, 15);
        
        BasketballGame.message();
        System.out.println();
        System.out.println("The total points scored was " + game.score() + ".");
        System.out.println("The percentage of free throws made was " + game.percentage("one") + "%.");
        System.out.println("The percentage of field goals made was " + game.percentage("two") + "%.");
        System.out.println("The percentage of three pointers made was " + game.percentage("three") + "%.");
    }
}