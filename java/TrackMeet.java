public class TrackMeet
{
 
 	public static void main (String[]args){
     	//Create the Mens100Meter Event
    	Event Mens100Meter = new Event();
     
     	//Enter the names and times for the following Runners
     	//Reinhart Wibisono, 9.9
     	//Ryan Vessels, 10.0
     	//Josh Scrivner, 10.1
     	//Mitchell Smith, 10.2
     	//Cameron Spry, 10.3
    	Mens100Meter.createRunner("Reinhart Wibisono", 9.9);
    	Mens100Meter.createRunner("Ryan Vessels", 10.0);
    	Mens100Meter.createRunner("Josh Scrivner", 10.1);
    	Mens100Meter.createRunner("Mitchell Smith", 10.2);
    	Mens100Meter.createRunner("Cameron Spry", 10.3);
     
     	//Find and print the average time in this Event
     	System.out.println(Mens100Meter.findAverageTime() + "\n");
     
     	//Find and print the name of the Runner who finished 3rd
     	System.out.println(Mens100Meter.findNameOfRunner(3) + "\n");
     
     	//Print the results of the Mens100Meter
    	System.out.print(Mens100Meter);
    }
}

