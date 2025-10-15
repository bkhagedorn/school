public class DreamVacationDriver
{
    public static void main(String[] args) {
        DreamVacation vacation1 = new DreamVacation();
        DreamVacation vacation2 = new DreamVacation("Quebec", 1000);
        
        vacation1.setDestination("Paris");
        vacation1.setCost(1300);
        
        System.out.print(vacation1 + "\n" + vacation2);
    }
}
