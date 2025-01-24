public class Song
{
    static int verseCounter=0;

    public static void verse(String animal,String noise)
    {
        verseCounter++;
        System.out.println("Old MacDonald had a farm");
        System.out.println("E-I-E-I-O");
        System.out.println("And on that farm he had a"+animal);
        System.out.println("E-I-E-I-O");
        System.out.println("With a"+noise+"-"+noise+"here");
        System.out.println("And a"+noise+"-"+noise+"there");
        System.out.println("here a "+noise+",there a "+noise);
        System.out.println("everywhere a"+noise+"-"+noise);
        System.out.println("Old Macdonald had a farm");

    }
    public static void main(String[] args)
    {
        verse("cow","moo");
        verse("duck","quack");
        verse("dog","woof");
    
    System.out.println("the verse method was called"+verseCounter+"times");
}}