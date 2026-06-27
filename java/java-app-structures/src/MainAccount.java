import bank.BankAccount;

public class MainAccount {
    public static void main(String[] args) {
        BankAccount account = new BankAccount();
        account.accountNumber = 78986;
        account.accountHolder = "Saally";
        account.balance = 1000000000000.0;

        System.out.println("Account number: " + account.accountNumber);
        System.out.println("Account holder: " + account.accountHolder);
        System.out.println("Account balance: " + account.balance);
    }
}
