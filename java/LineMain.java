public class LineMain
{
    public static void main(String[] args) {
        Line line = new Line();
        System.out.println(line.toString());
        System.out.println("Distance: " + Double.toString(line.getDist()));
        System.out.print("Slope: " + Double.toString(line.getSlope()));
    }
}