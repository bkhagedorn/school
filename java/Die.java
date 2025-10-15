public class Die{
    private int faceValue, numSides;
    
    public Die(){
        faceValue = 1;
        numSides = 6;
    }
    
    public Die(int x){
        faceValue = 1;
        numSides = x;
    }
    
    public int roll(){
        faceValue = (int)(Math.random() * (numSides + 1));
        return faceValue;
    }
    
    public int getFaceValue(){
        return faceValue;
    }
    
    public void setFaceValue(int value){
        faceValue = value;
    }
    
    public static void message(){
        System.out.println("Rolling...");
    }
    
    public String toString(){
        String result = "faceValue=" + faceValue + " numSides=" + numSides;
        return result;
    }
}