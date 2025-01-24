package basic;

public class add_sub {
    private int a;
    private int b;

    public void sum()
    {
        System.out.println(a+b);

    }
    public void sub()
    {
        System.out.println(a-b);
    }
    public void setValues(int a, int b)
    {
        this.a=a;
        this.b=b;
    }
    
}

class Main {
        public static void main(String[] args) {
            add_sub obj = new add_sub();
            obj.setValues(10, 9);


            obj.sum();
            obj.sub();
        }
    }