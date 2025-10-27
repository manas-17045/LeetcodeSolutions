// Leetcode 2043: Simple Bank System
// https://leetcode.com/problems/simple-bank-system/
// Solved on 26th of October, 2025
class Bank {

    private long[] balance;
    private int n;

    public Bank(long[] balance) {
        this.balance = balance;
        this.n = balance.length;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if (account1 < 1 || account1 > n || account2 < 1 || account2 > n) {
            return false;
        }
        
        int index1 = account1 - 1;
        int index2 = account2 - 1;
        
        if (balance[index1] >= money) {
            balance[index1] -= money;
            balance[index2] += money;
            return true;
        }
        
        return false;
    }
    
    public boolean deposit(int account, long money) {
        if (account < 1 || account > n) {
            return false;
        }
        
        int index = account - 1;
        balance[index] += money;
        return true;
    }
    
    public boolean withdraw(int account, long money) {
        if (account < 1 || account > n) {
            return false;
        }
        
        int index = account - 1;
        
        if (balance[index] >= money) {
            balance[index] -= money;
            return true;
        }
        
        return false;
    }
}