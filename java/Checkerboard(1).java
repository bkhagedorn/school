import java.util.*;
public class Checkerboard{
    public static boolean check(int[] array, int check){
        for (int i : array){
            if (i == check)
                return true;
        }
        return false;
    }
    
    public static void main(String[] args) {
        char[][] checkerboard = new char[4][5];
        Random rand = new Random();
        int randomRow = -9, randomColumn = -9;
        boolean check1 = false;
        int[] randomRows = {-1, -1, -1, -1}, randomColumns = {-1, -1, -1, -1, -1};
        for (int i = 0; i < checkerboard.length; i++){
            for (int x = 0; x < checkerboard[i].length; x++){
                checkerboard[i][x] = '-';
            }
        }
        
        //1
        for (int i = 0; i < checkerboard.length; i++){
            for (int x = 0; x < checkerboard[i].length; x++){
                System.out.print(checkerboard[i][x] + "\t");
            }
            System.out.println();
        }
        
        System.out.println();
        
        //2
        for (int i = 0; i < 5; i++){
            while (check1 == false)
                randomRow = rand.nextInt(4);
                check1 = check(randomRows, randomRow);
            while (check(randomColumns, randomColumn) == false)
                randomColumn = rand.nextInt(5);
            checkerboard[randomRow][randomColumn] = 'X';
            randomRows[i] = randomRow;
            randomColumns[i] = randomColumn;
        }
        for (int i = 0; i < checkerboard.length; i++){
            for (int x = 0; x < checkerboard[i].length; x++){
                System.out.print(checkerboard[i][x] + "\t");
            }
            System.out.println();
        }
    }
}
