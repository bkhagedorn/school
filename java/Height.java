public class Height{
    private int ft;
    private int in;
    
    public Height(int a, int b){
        ft = a;
        in = b;
        this.simplify();
    }
    public Height(int a){
        in = a;
        this.simplify();
    }
    
    public void simplify(){
        while (in >= 12){
            in -= 12;
            ft += 1;
        }
    }
    
    public void add(int a){
        in += a;
        this.simplify();
    }
    public void add(Height ogfortnite){
        in += ogfortnite.getInches();
        ft += ogfortnite.getFeet();
        this.simplify();
    }
    
    public int getInches(){
        return in;
    }
    public int getFeet(){
        return ft;
    }
    
    public String toString(){
        return ft + " feet " + in + " inches";
    }
}