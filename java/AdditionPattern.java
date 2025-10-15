public class AdditionPattern{
    private int firstNum, iter, currentNum;
    
    //iter is the amount added after each iteration of the pattern
    
    public AdditionPattern(int a, int b){
        firstNum = a;
        currentNum = a;
        iter = b;
    }
    
    public int currentNumber(){
        return currentNum;
    }
    
    public void next(){
        currentNum += iter;
    }
    
    public void prev(){
        if (currentNum != firstNum)
            currentNum -= iter;
    }
}