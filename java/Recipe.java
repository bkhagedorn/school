import java.util.*;
public class Recipe{
    public static void main(String[] args) {
        ArrayList<String> ingredients = new ArrayList<String>();
        ingredients.add("flour");
        ingredients.add("sugar");
        ingredients.add("cocoa");
        ingredients.add("oil");
        ingredients.add("butter");
        ingredients.add("eggs");
        
        System.out.println("To make a cake, use these " + ingredients.size() + " ingredients:");
        System.out.println(ingredients + "\n");
        System.out.println("My favorite ingredient is " + ingredients.get(2) + ".\n");
        System.out.println("Let's replace cocoa with vanilla!");
        ingredients.set(2, "vanilla");
        System.out.println(ingredients + "\n");
        System.out.println("Let's try it with cocoa AND vanilla!");
        ingredients.add(2, "cocoa");
        System.out.println(ingredients + "\n");
        System.out.println("Yuck, it's better with just cocoa.");
        ingredients.remove(3);
        System.out.println(ingredients + "\n");
        
        for (int i = 0; i < ingredients.size(); i++){
            System.out.println(ingredients.get(i));
        }
        System.out.println();
        for (String i : ingredients){
            System.out.println(i);
        }
    }
}
