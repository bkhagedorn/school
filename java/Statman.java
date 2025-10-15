public class Statman
{
    private double[] classDistribution;
    public Statman(double[] scores){
        classDistribution = scores;
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
}

