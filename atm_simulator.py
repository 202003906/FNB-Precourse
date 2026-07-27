balance = 500

withdrawal_amount = float(input("Enter amount to withdraw: R"))

if withdrawal_amount <= 0:
        print("Invalid amount. You must withdraw more than R0.")
elif withdrawal_amount <= balance:
    balance = balance - withdrawal_amount
    print(f"Withdrawal successful! Remaining balance: R{balance}")
else:
    print("Declined. Insufficient funds")