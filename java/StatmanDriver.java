public class StatmanDriver{
 	public static void main(String args[]){
      	double[] testScores = {85, 88, 89, 77, 99, 91, 66, 48, 77, 77};
      	Statman class1Stats = new Statman(testScores);
      	System.out.print("Grade Distribution: ");
      	for (double i : class1Stats.getDistribution()){
      	    System.out.print(i + " ");
      	}
      	System.out.println();
      	System.out.println("mean: " + class1Stats.evalMean());
      	System.out.print("range: " + class1Stats.evalRange());
 	}
}
