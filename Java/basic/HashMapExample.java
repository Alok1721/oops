//1.public class should be define with same name as class. and in one file only one public class should be there.
//
import java.util.HashMap;
import java.util.Map;
class employee {
    private String name;
    private int employeeId;
    private int departmentId;
    
    public void setVariable(int employeeId,String name,int departmentId)
    {
        this.name=name;
        this.employeeId=employeeId;
        this.departmentId=departmentId;
    }

    public Map<String,Object> getDetails()
    {
        Map<String,Object>details=new HashMap<>();
        details.put("employee_id",employeeId);
        details.put("name",name);
        details.put("department_id",departmentId);
        return details;
    }
    
    
}

public class HashMapExample {
    
    public static void main(String[] args)
    {
        employee obj=new employee();
        obj.setVariable(1,"alok",1);
        Map<String,Object> details=obj.getDetails();
        for(Map.Entry<String,Object> entry:details.entrySet())
        {
            System.out.println(entry.getKey()+":"+entry.getValue());
        }
    }

}
