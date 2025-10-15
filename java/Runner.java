public class Runner{	
    private String name;
    private double time;
 	//instance fields
    public Runner (String a, double b){
     	name = a;
     	time = b;
    }
     
    //return the time for the Runner
    public double getTime(){
        return time; 
    }
     
    //return the name for the runner
    public String getName(){
        return name;
    }
     
    public String toString(){
        return name + ": " + time; 
    }
}
 
