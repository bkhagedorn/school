public class DreamVacation{
    private String destination;
    private double cost;
    
    public DreamVacation(){
        ;
    }
    public DreamVacation(String a, double b){
        destination = a;
        cost = b;
    }
    
    public String getDestination(){
        return destination;
    }
    public double getCost(){
        return cost;
    }
    
    public void setDestination(String a){
        destination = a;
    }
    public void setCost(double a){
        cost = a;
    }
    
    public String toString(){
        return "Destination: " + destination + "\tCost: $" + cost;
    }
}