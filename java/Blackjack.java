import java.util.*;
public class Blackjack{
    private static Random rand = new Random();
    private static List<Integer> dealerCards = new ArrayList<>(), playerCards = new ArrayList<>();
    private static Card card = new Card();
    private static boolean done = false, giveUp = false;
    
    private static void start(){
        card.draw();
        dealerCards.add(card.value());
        card.draw();
        dealerCards.add(card.value());
            
        card.draw();
        playerCards.add(card.value());
        card.draw();
        playerCards.add(card.value());

        done = false;
        giveUp = false;
    }
    
    private static int totalValue(String player){
        int total = 0;
        if (player.equals("dealer")){
            for (int i = 1; i < dealerCards.size(); i++){
                total += dealerCards.get(i);
            }
        }
        else if (player.equals("player")){
            for (int i = 0; i < playerCards.size(); i++){
                total += playerCards.get(i);
            }
        }
        return total;
    }
    
    private static void option(String opt){
        if (opt == "draw"){
            card.draw();
            playerCards.add(card.value());
        }
    }
    
    private static void endTurn(){
        card.draw();
        dealerCards.add(card.value());
    }
    
    private static String getDealerCards(){
        String newStr = "[?, ";
        for (int i = 1; i < dealerCards.size(); i++){
            if (i != dealerCards.size()-1)
                newStr += dealerCards.get(i) + ", ";
            else
                newStr += dealerCards.get(i);
        }
        return newStr + "]";
    }
    
    public static void main(String[] args) {
        int totalMoney = 100, bet, choice;
        String cont;
        Scanner scan = new Scanner(System.in);
        
        while (totalMoney != 0){
            System.out.print("How much would you like to bet? ($" + totalMoney + ")");
            bet = scan.nextInt();
            while (bet > totalMoney){
                System.out.print("You can't bet that much.");
                bet = scan.nextInt();
            }
            totalMoney -= bet;
            Blackjack.start();
            while (Blackjack.totalValue("player") >= 21 || Blackjack.totalValue("dealer") >= 21){
                Blackjack.start();
            }
            while (!done){
                System.out.println("What will you do?");
                System.out.println("Your cards: " + playerCards);
                System.out.println(Blackjack.totalValue("player"));
                System.out.println("Dealer's cards: " + Blackjack.getDealerCards());
                System.out.println("?+" + Blackjack.totalValue("dealer"));
                
                System.out.println();
                System.out.println("[1] - Draw Cards");
                System.out.print("[2] - Stand");
                choice = scan.nextInt();
                if (choice == 1)
                    Blackjack.option("draw");
                else{
                    while (Blackjack.totalValue("dealer") <= 21 && Blackjack.totalValue("dealer") < Blackjack.totalValue("player")){
                        if (Math.abs(Blackjack.totalValue("dealer") - Blackjack.totalValue("player")) <= 3 && rand.nextInt(3) == 0){
                            giveUp = true;
                            break;
                        }
                        Blackjack.endTurn();
                        System.out.println();
                        System.out.println("Your cards: " + playerCards);
                        System.out.println(Blackjack.totalValue("player"));
                        System.out.println("Dealer's cards: " + Blackjack.getDealerCards());
                        System.out.println("?+" + Blackjack.totalValue("dealer"));
                        try {
                            Thread.sleep(2000);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
                
                if (Blackjack.totalValue("player") == 21 || Blackjack.totalValue("dealer") > 21 || giveUp){
                    System.out.println("Your cards: " + playerCards);
                    System.out.println(Blackjack.totalValue("player"));
                    System.out.println("You win!");
                    bet *= 2;
                    totalMoney += bet;
                    done = true;
                }
                else if (Blackjack.totalValue("player") > 21 || Blackjack.totalValue("dealer") == 21 || (Blackjack.totalValue("dealer") < 21 && Blackjack.totalValue("dealer") > Blackjack.totalValue("player"))){
                    System.out.println("You lost.");
                    done = true;
                }
                
            }
            playerCards.clear();
            dealerCards.clear();
        }
    }
}
