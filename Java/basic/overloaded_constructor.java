class overloaded_constructor
{
    private String name;
    private int id;
    private String department;

    public overloaded_constructor(String name)
    {
        this.name=name;
    }
    public overloaded_constructor(String name,int id)
    {
        this.name=name;
        this.id=id;
    }
    public overloaded_constructor(String name,int id,String department)
    {
        this.name=name;
        this.id=id;
        this.department=department;
    }
    public void displayDetails()
    {
        System.out.println("Name:"+name);
        if(id!=0)
        {
            System.out.println("id:"+id );
            
        }
        if(department!=null)
        {
            System.out.println("Department:"+department);

        }
       System.out.println("\n-------------");
    }
    public static void main(String[] args)
    {
        overloaded_constructor emp1=new overloaded_constructor("Alok");
        emp1.displayDetails();
        overloaded_constructor emp2=new overloaded_constructor("Alok",1);
        emp2.displayDetails();
        overloaded_constructor emp3=new overloaded_constructor("Alok",2,"Zine");
        emp3.displayDetails();
    }
}