public class Line{
    private int x1, x2, y1, y2;
    
    public Line(){
        x1 = (int)(Math.random() * 800);
        x2 = (int)(Math.random() * 800);
        y1 = (int)(Math.random() * 600);
        y2 = (int)(Math.random() * 600);
    }
    
    public double getDist(){
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(x2 - x1, 2));
    }
    
    public double getSlope(){
        return (double)(y2 - y1) / (x2 - x1);
    }
    
    public String toString(){
        return "(" + Integer.toString(x1) + ", " + Integer.toString(y1) + "), (" + Integer.toString(x2) + ", " + Integer.toString(y2) + ")";
    }
}