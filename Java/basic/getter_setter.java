//1. new keyword important for array defination & zero automatically assign to on array creation 2.array are dynamically allocated  3.find the length of array by length property  4. Objects of java store in heap segment. 5. type var-name[]; or type[] var-name , both is correct way 
//2. object store iin heap but reference store in stack
//3. by return objects we can print return different datatype using same method no need to create the separate method for integer or string returning
//4. casting of various variable naming and elements. 
//5. returning object user must know the order of element acess. if longer data then map will be better because knowing about index will be difficult.

class Employee{
    private String name;
    private int employeeId;
    private int departmentId;

    public void setVariable(int employeeId,String name,int departmentId){
        this.name=name;
        this.employeeId=employeeId;
        this.departmentId=departmentId;
    }


    public Object[] getVariable()
    {
        
        return new Object[]{employeeId,departmentId,name};
    }


}

public class getter_setter{
    public static void main(String[] args){
        Employee obj=new Employee();
        obj.setVariable(1,"alok", 1);
        Object[] temp=obj.getVariable();

            System.out.println("employee id:"+temp[0]);
            System.out.println("Department id:"+temp[1]);
            System.out.println("Employee Name:"+temp[2]);
        
    
    }
    
}