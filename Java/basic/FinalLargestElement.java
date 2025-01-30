//1.constructor is created to assign the value during creation of new objects.
public class FinalLargestElement {
    private int[] num;
    public FinalLargestElement(int[] numbers)//constructor to assign the values
    {
        this.num=numbers;
    }

    public void display()
    {
        if(num==null ||num.length==0)
        {
            System.out.println("Array is empty.");
            return;
        }

        int l=num[0];
        for(int n:num)
        {
            if(n>l)
            {
                l=n;
            }
        }

        System.out.println("the largest element is:"+l);
    }

    public static void main(String[] args)
    {
        int[] arr={10,20,30,40,25};
        FinalLargestElement obj=new FinalLargestElement(arr);
        obj.display();
    }
}
