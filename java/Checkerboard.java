import java.util.*;
public class Checkerboard{
    public static void main(String[] args) {
        char[][] checkerboard = new char[4][5];
        Random rand = new Random();
        int randRow = rand.nextInt(4), randColumn = rand.nextInt(5);
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
            while (checkerboard[randRow][randColumn] == 'X'){
                randRow = rand.nextInt(4);
                randColumn = rand.nextInt(5);
            }
            checkerboard[randRow][randColumn] = 'X';
        }
        for (int i = 0; i < checkerboard.length; i++){
            for (int x = 0; x < checkerboard[i].length; x++){
                System.out.print(checkerboard[i][x] + "\t");
            }
            System.out.println();
        }
        
        System.out.println();
        
        //3
        for (int i = 0; i < 5; i++){
            while (checkerboard[randRow][randColumn] == 'X' || checkerboard[randRow][randColumn] == 'O'){
                randRow = rand.nextInt(4);
                randColumn = rand.nextInt(5);
            }
            checkerboard[randRow][randColumn] = 'O';
        }
        for (int i = 0; i < checkerboard.length; i++){
            for (int x = 0; x < checkerboard[i].length; x++){
                System.out.print(checkerboard[i][x] + "\t");
            }
            System.out.println();
        }
    }
}
