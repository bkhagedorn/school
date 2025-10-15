public class Hotel extends Building{
    private int occupants = 2000;
    private int remodeledRooms = 100;
    
    public void occupantsMessage(){
        System.out.println("Number of occupants: " + occupants);
        System.out.println("Occupants per room: " + (occupants/super.getRooms()));
    }
    
    public void roomMessage(){
        System.out.print("Out of the " + super.getRooms() + " rooms, " + remodeledRooms + " are newly remodeled.");
    }
    
    public void getBuildingsRoomMessage(){
        super.roomMessage();
    }
}