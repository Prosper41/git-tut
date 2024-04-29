class BankAccount {
    constructor(accountNumber, balance = 0) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    deposit(amount) {
        if (amount > 0) {
            this.balance += amount;
            console.log(`Deposited $${amount}. New balance: $${this.balance}`);
        } else {
            console.log("Invalid deposit amount.");
        }
    }

    withdraw(amount) {
        if (amount > 0 && amount <= this.balance) {
            this.balance -= amount;
            console.log(`Withdrew $${amount}. New balance: $${this.balance}`);
        } else {
            console.log("Invalid withdrawal amount or insufficient funds.");
        }
    }
}

// Example usage
const account1 = new BankAccount("1234567890", 1000);
console.log(`Account Number: ${account1.accountNumber}`);
console.log(`Current Balance: $${account1.balance}`);

account1.deposit(500);
account1.withdraw(200);
account1.withdraw(1500);
account1.deposit(100)