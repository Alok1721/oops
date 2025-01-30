///Q).Rectangle with attributes of length and width ,by default 1. and get and set methods for both attributes. adn methods to create the area of rectangle.

///1.modification of any private variable and function overloading with different arguments. 
public class RectangleArea {
    private double length;
    private double width;

    public RectangleArea()
    {
        this.length=1;
        this.width=1;
    }
    
    public RectangleArea(double length,double width)
    {
        this.length=length;
        this.width=width;
    }

    public double getLength()
    {
        return length;
    }

    public void setLength(double length)
    {
        if(length>0)
        {
            this.length=length;
        }else{
            System.out.println("length must be positive");
        }
    }

    public double getWidth()
    {
        return width;
    }

    public void setWidth(double width)
    {
        if(width>0)
        {
            this.width=width;
        }else{
            System.out.println("width must be positive");
        }
    }

    public double calculateArea()
    {
        return length*width;
    }

    public static void main(String[] args)
    {
        RectangleArea obj=new RectangleArea();

        System.out.println("Default Area:"+obj.calculateArea());

        obj.setLength(5);
        obj.setWidth(5);
        System.out.println("Default Area:"+obj.calculateArea());
        
    }

}
