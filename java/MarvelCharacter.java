public class MarvelCharacter{
    private String name;
    private String power;
    private int comics;
    private static int numChars = 0;
    
    public MarvelCharacter(){
        numChars++;
    }
    public MarvelCharacter(String a, String b, int c){
        name = a;
        power = b;
        comics = c;
        numChars++;
    }
    
    public static int getNumCharacters(){
        return numChars;
    }
    
    public String getName(){
        return name;
    }
    public String getPower(){
        return power;
    }
    public int getComicsAppeared(){
        return comics;
    }
    
    public void changePower(String a){
        power = a;
    }
    public void setComicsAppeared(int a){
        comics = a;
    }
    public void changeName(String a){
        name = a;
    }
    
    public String toString(){
        return "Name: " + name + "\nPower: " + power + "\nComics: " + comics;
    }
}