public class HeightMain
{
    public static void main(String[] args) {
        Height bAdams = new Height(7, 8);
        Height vTroyer = new Height(2, 8) ;
        Height kid = new Height(36);
        Height dParton = new Height(60);
        
        System.out.println("Brendan Adams: " + bAdams);
        System.out.println("Vern Troyer: " + vTroyer);
        System.out.println("Little Kid: " + kid);
        System.out.println("Dolly Parton: " + dParton);
        
        kid.add(4);
        dParton.add(vTroyer);
        
        System.out.println();
        System.out.println("Brendan Adams: " + bAdams);
        System.out.println("Vern Troyer: " + vTroyer);
        System.out.println("Little Kid: " + kid);
        System.out.println("Dolly Parton: " + dParton);
    }
}
