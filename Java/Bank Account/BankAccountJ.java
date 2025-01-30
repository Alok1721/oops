///Q). Create a class BankAccountJ with members AcctNo, balance, and AcctType. Implement the following operations:
///a) Deposit an amount of 10,000.
///b) Withdraw an amount of 5,000.
///c) Display account details.

//
public class BankAccountJ {
    private int acctNo;
    private double balance;
    private String acctType;

    public BankAccountJ(int acctNo,double balance,String acctType)
    {
        this.acctNo=acctNo;
        this.balance=balance;
        this.acctType=acctType;
    }

    public void deposit(double amount)
    {
        this.balance=this.balance+amount;
    }
    public void getAccountType()
    {
        System.out.println("Account type:"+acctType);
    }

    public void withdraw(double amount)
    {
        if(balance<amount)
        {
            System.out.println("Insufficient Balance!!");
            return ;
        }

        this.balance=this.balance-amount;
    }
    public void getBalance()
    {
        System.out.println("account no:"+acctNo+" Balance amount:"+balance);
    }

    public static void main(String[] args)
    {
        BankAccountJ obj=new BankAccountJ(1,10000,"current");
        obj.deposit(10000);
        obj.getBalance();
        obj.withdraw(5000);
        obj.getBalance();
        obj.getAccountType();
    }
}
