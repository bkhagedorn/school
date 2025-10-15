public class Statman2Driver{
 	public static void main(String args[]){
      	double[] testScores = {85, 88, 89, 77, 99, 91, 66, 48, 53, 86};
      	String[] names = {"student1", "student2", "student3", "student4", "student5", "student6", "student7", "student8", "student9", "student10"};
      	Statman2 class1Stats = new Statman2(testScores, names);
      	System.out.println(class1Stats.findGrade("student4"));
      	System.out.println(class1Stats.findGrade2("student7") + "\n");
      	class1Stats.sortGrades();
      	for (double i : class1Stats.getDistribution()){
      	    System.out.print(i + " ");
      	}
      	System.out.println();
      	for (String i : class1Stats.getNames()){
      	    System.out.print(i + " ");
      	}
      	System.out.println("\n");
      	System.out.print(class1Stats.findMedian());
 	}
}
