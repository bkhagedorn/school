public class Triangle{
    private int angle1, angle2, angle3;
    
    public Triangle(int a, int b, int c){
        angle1 = a;
        angle2 = b;
        angle3 = c;
    }
    
    public boolean isTriangle(){
        if (angle1 + angle2 + angle3 == 180)
            return true;
        return false;
    }
}