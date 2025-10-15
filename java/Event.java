public class Event
{
    //instance variable is an array of 5 runners
    private Runner[] runners = new Runner[5];
    private int count = 1;
     
    //create a Runner and place them into the array of Runners.
    //precondition: exactly 5 Runners will be created for this Event
    //param name the name of the Runner
    //param time the time for the Runner in this event
    public void createRunner(String name, double time){
    	if (count <= 5){
    		runners[count-1] = new Runner(name, time);
    		count++;
        }
    }
     
    //return the average time of the runners in this Event
    public double findAverageTime(){
    	double ave = 0;
        for (Runner i : runners){
            ave += i.getTime();
        }
        return ave / count;	
    }
     
    //precondition: Runners have been entered into an array
    //from lowest to highest time
    //param place the place finished in the race by a Runner
    //return the name of the Runner who finished this place
    public String findNameOfRunner(int place){
        return runners[place-1].getName(); 	 
    }
     
    //return names and times of all 5 runners
    public String toString(){
    	String str = "";
        for (Runner i : runners){
    		str += i + "\n";
    	}
    	return str;
    }
}
