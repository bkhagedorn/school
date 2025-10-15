public class TriangleMain
{
    public static void main(String[] args) {
        Triangle tri = new Triangle(60, 60, 60);
        if (tri.isTriangle())
            System.out.print("These angles will form a triangle.");
        else
            System.out.print("These angles will not form a triangle.");
    }
}