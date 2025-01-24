//1. we can reference to base class but we can initalize with another another class then initialized class method will return when we will call.
//2. father is subclass of person it mean father is object of person.
//3. without subclass, we cannot give reference. we can only create object of same class or subclass.

package polymorphism;
class Person{
    void role()
    {
        System.out.println("I am person");
    }
}

class Father extends Person{
    @Override
    void role()
    {
        System.out.println("I am father");
    }
}
class Husband extends Father{
    @Override
    void role()
    {
        System.out.println("I am Husband");
    }
}



public class overriding {
    

    public static void main(String [] args)
    {
        Person p=new Father();
        Father h=new Husband();

        p.role();
        h.role();
    }
}
