public class TwoDArrayMain{
    public static void main(String[] args){
        TwoDArrayPractice lala = new TwoDArrayPractice();
        
        //1
        int[][] arr1 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        lala.rowSwap(arr1, 0, 2);
        for (int[] i : arr1){
            for (int j = 0; j < i.length; j++){
                if (j < i.length-1)
                    System.out.print(i[j] + ", ");
                else
                    System.out.print(i[j]);
            }
            System.out.println();
        }
        
        System.out.println();
        
        //2
        int[][] arr2 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        lala.colSwap(arr2, 0, 1);
        for (int[] i : arr2){
            for (int j = 0; j < i.length; j++){
                if (j < i.length-1)
                    System.out.print(i[j] + ", ");
                else
                    System.out.print(i[j]);
            }
            System.out.println();
        }
        
        System.out.println();
        
        //3
        for (String[] i : lala.fillRowMajor("testing!", 2, 4)){
            for (int j = 0; j < i.length; j++){
                if (j < i.length-1)
                    System.out.print(i[j] + ", ");
                else
                    System.out.print(i[j]);
            }
            System.out.println();
        }
        
        System.out.println();
        
        //4
        int[] arr3 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        for (int[] i : lala.fillColumnMajor(arr3, 2, 4)){
            for (int j = 0; j < i.length; j++){
                if (j < i.length-1)
                    System.out.print(i[j] + ", ");
                else
                    System.out.print(i[j]);
            }
            System.out.println();
        }
    }
}
