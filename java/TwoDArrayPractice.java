class TwoDArrayPractice{
    /**
     * Swaps all values in the specified 2 rows of mat.
     * @param mat the array
     * @param rowAIndex the index of a row to be swapped
     * @param rowBIndex the index of a row to be swapped
     */
    public void rowSwap(int[][] mat, int rowAIndex, int rowBIndex){
        int[] temp = mat[rowAIndex];
        mat[rowAIndex] = mat[rowBIndex];
        mat[rowBIndex] = temp;
    }
    

    /**
     * Swaps all values in the specified 2 columns of mat.
     * @param mat the array
     * @param colAIndex the index of a column to be swapped
     * @param colBIndex the index of a column to be swapped
     */
    public void colSwap(int[][] mat, int colAIndex, int colBIndex){
        int[] temp = new int[mat.length];
        for (int i = 0; i < temp.length; i++){
            temp[i] = mat[i][colAIndex];
        }
        for (int i = 0; i < temp.length; i++){
            mat[i][colAIndex] = mat[i][colBIndex];
        }
        for (int i = 0; i < temp.length; i++){
            mat[i][colBIndex] = temp[i];
        }
    }

    
    /**
     * Returns an array with the specified number of rows and columns
     * containing the characters from str in row-major order. If str.length()
     * is greater than rows * cols, extra characters are ignored. If
     * str.length() is less than rows * cols, the remaining elements in the
     * returned array contains null.
     * 
     * @param str the string to be placed in an array
     * @param rows the number of rows in the array to be returned
     * @param cols the number of columns in the array to be returned
     * @return an array containing the characters from str in row-major order
     */
    public String[][] fillRowMajor(String str, int rows, int cols){
        String[][] arr = new String[rows][cols];
        int count = 0;
        for (int i = 0; i < arr.length; i++){
            for (int j = 0; j < arr[i].length; j++){
                if (count < str.length()){
                    arr[i][j] = Character.toString(str.charAt(count));
                    count++;
                }
                else
                    arr[i][j] = null;
            }
        }
        return arr;
    }

    
    /**
     * Returns an array containing the elements of vals in column-major order.
     * 
     * Precondition: vals.length == rows * cols
     * 
     * @param vals the elements
     * @param rows the number of rows in the array to be returned
     * @param cols the number of columns in the array to be returned
     * @return an array containing the elements of vals in column-major order
     */
    public int[][] fillColumnMajor(int[] vals, int rows, int cols){
        int[][] arr = new int[rows][cols];
        int count = 0;
        for (int j = 0; j < arr[0].length; j++){
            for (int i = 0; i < arr.length; i++){
                if (count < vals.length){
                    arr[i][j] = vals[count];
                    count++;
                }
                else
                    arr[i][j] = -1;
            }
        }
        return arr;
    }
}