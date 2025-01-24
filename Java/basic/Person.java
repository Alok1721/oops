public class Person
{
    private String name;
    private String email;
    private String phoneNumber;
    public static int personCounter=0;

    public static void printPersonCounter()
    {
        System.out.println("Person counter:"+personCounter);
    }
    //settter method to update the private value of class
    public Person(String initName,String initEmail,String initPhone)
    {
        name=initName;
        email=initEmail;
        phoneNumber=initPhone;
        personCounter++;

    }

    public String toString()
    {
        return name+":"+email+":"+phoneNumber;
    }

    public static void main(String[] args)
    {
        Person p1=new Person("alok","alokdhiraj1234@gmail.com","8882806064");
    
        p1.printPersonCounter();
    }

}