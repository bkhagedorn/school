public class GradeRange{
    public static void main (String[] args){
        Grade[] grades = {new Grade("A", 95), new Grade("A-", 90), new Grade("B+", 87), new Grade("B", 83), new Grade("B-", 80), new Grade("C+", 77), new Grade("C", 73), new Grade("C-", 70), new Grade("D+", 67), new Grade("D", 63), new Grade("D-", 60), new Grade("F", 0)};
        for (int i = 0; i < grades.length; i++){
            System.out.println(grades[i].getGrade() + "\t" + grades[i].getCutoff());
        }
    }
}