package main

import "fmt"

type BankAccount struct {
    accountNumber string
    balance       float64
}

func (b *BankAccount) deposit(amount float64) {
    if amount > 0 {
        b.balance += amount
        fmt.Printf("Deposited $%.2f. New balance: $%.2f\n", amount, b.balance)
    } else {
        fmt.Println("Invalid deposit amount.")
    }
}

func (b *BankAccount) withdraw(amount float64) {
    if amount > 0 && amount <= b.balance {
        b.balance -= amount
        fmt.Printf("Withdrew $%.2f. New balance: $%.2f\n", amount, b.balance)
    } else {
        fmt.Println("Invalid withdrawal amount or insufficient funds.")
    }
}

func main() {
    account1 := BankAccount{accountNumber: "1234567890", balance: 1000}
    fmt.Printf("Account Number: %s\n", account1.accountNumber)
    fmt.Printf("Current Balance: $%.2f\n", account1.balance)

    account1.deposit(500)
    account1.withdraw(200)
    account1.withdraw(1500)
}
