public class Donuts{
    private int glazed, john, cream;
    
    public Donuts(int a, int b, int c){
        glazed = a;
        john = b;
        cream = c;
    }
    
    public double cost(){
        return (glazed * 0.85) + (john * 1.20) + (cream * 1.55);
    }
    
    public String toString(){
        return "Glazed: " + Integer.toString(glazed) + ", Long Johns: " + Integer.toString(john) + ", Cream Filled: " + Integer.toString(cream);
    }
}