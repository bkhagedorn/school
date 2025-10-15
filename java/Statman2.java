public class Statman2
{
    private double[] classDistribution;
    private String[] classNames;
    public Statman2(double[] scores, String[] names){
        classDistribution = scores;
        classNames = names;
    }
    
    public double[] getDistribution(){
        return classDistribution;
    }
    
    public double evalMean(){
        double sum = 0;
        for (double i : classDistribution){
            sum += i;
        }
        return sum / classDistribution.length;
    }
    
    public double evalRange(){
        double lowest = classDistribution[0];
        double highest = classDistribution[0];
        for (double i : classDistribution){
            if (i < lowest)
                lowest = i;
            if (i > highest)
                highest = i;
        }
        return highest - lowest;
    }
    
    public double findGrade(String name){
        for (int i = 0; i < classNames.length; i++){
            if (classNames[i].equals(name))
                return classDistribution[i];
        }
        return -1;
    }
    
    public double findGrade2(String name){
        int low = 0, high = classNames.length - 1, mid = (low + high) / 2;
        while (classNames[mid].equals(name) == false && low <= high){
            if (classNames[mid].compareTo(name) > 0)
                high = mid - 1;
            else
                low = mid + 1;
            mid = (low + high) / 2;
        }
        if (classNames[mid].equals(name))
            return classDistribution[mid];
        else
            return -1;
    }
    
    public void sortGrades(){
        int num;
        double temp1;
        String temp2;
        for (int i = 0; i < classDistribution.length; i++) {
            num = i;
            for (int x = i + 1; x < classDistribution.length; x++) {
                if (classDistribution[x] < classDistribution[num]) {
                    num = x;
                }
            }
            if (num != i) {
                temp1 = classDistribution[i];
                classDistribution[i] = classDistribution[num];
                classDistribution[num] = temp1;
                
                temp2 = classNames[i];
                classNames[i] = classNames[num];
                classNames[num] = temp2;
            }
        }
    }
    
    public String[] getNames(){
        return classNames;
    }
    
    public double findMedian(){
        return classDistribution[(classDistribution.length - 1) / 2];
    }
}
