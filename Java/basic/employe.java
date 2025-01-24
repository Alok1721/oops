//1. static method should be called through employe name but not throught object.
//2.non static method cannot be called by static method.

//1.static method tied directly with class while non static method tied with object of class
//2.
public class employe {
    static String Employee_name;
    static double Employee_salary;

    static void set(String n,double p)
        {
            Employee_name=n;
            Employee_salary=p;
    }
    static void get()
    {
        employe.set("dhiraj",20);
        System.out.println("Employee name is"+Employee_name);
        System.out.println("Employee CTC is"+Employee_salary);
        
    }

    public static void main(String main[])
    {
        // employe obj=new employe();
        employe.set("alok",20.0);
        employe.get();
    }
}
