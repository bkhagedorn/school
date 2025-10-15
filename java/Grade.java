public class Grade
{
    private String grade;
    private int cutoff;
    public Grade(String a, int b){
        grade = a;
        cutoff = b;
    }
    
    public String getGrade(){
        return grade;
    }
    
    public int getCutoff(){
        return cutoff;
    }
}
