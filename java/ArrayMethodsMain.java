public class ArrayMethodsMain
{
    public static void main(String[] args) {
        String[] array1 = {"Venom", "Spider-Man", "Bucky", "Luna Snow", "Jeff"};
        int[] array2 = new int[10];
        double[] array3 = new double[10];
        
        for (int i = 1; i <= 10; i++){
            array2[i-1] = i;
        }
        for (int i = 1; i <= 10; i++){
            array3[i-1] = i*5;
        }
        
        ArrayMethods.printOnOne(array1);
        System.out.println("\n");
        ArrayMethods.printIt(array1);
        System.out.println("\n");
        System.out.println(ArrayMethods.addIt(array2));
        System.out.println(ArrayMethods.addIt(array3));
        System.out.println(ArrayMethods.average(array2));
        System.out.println(ArrayMethods.average(array3));
    }
}
