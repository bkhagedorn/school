public class ArrayMethods{
    public static void printOnOne(String[] a){
        for (String i : a){
            System.out.print(i + "  ");
        }
    }
    
    public static void printIt(String[] a){
        for (String i : a){
            System.out.print(i);
            if (!i.equals(a[a.length-1]))
                System.out.print("\n");
        }
    }
    
    public static int addIt(int[] a){
        int total = 0;
        for (int i : a){
            total += i;
        }
        return total;
    }
    public static double addIt(double[] a){
        double total = 0;
        for (double i : a){
            total += i;
        }
        return total;
    }
    
    public static double average(int[] a){
        double total = 0;
        int nums = 0;
        for (int i : a){
            total += i;
            nums++;
        }
        return total/nums;
    }
    public static double average(double[] a){
        double total = 0;
        int nums = 0;
        for (double i : a){
            total += i;
            nums++;
        }
        return total/nums;
    }
}