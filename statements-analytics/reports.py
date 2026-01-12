# reports.py

transactions = []

n = int(input("How many transactions do you want to enter? "))

for i in range(n):
    date = input(f"Enter date for transaction {i+1} (YYYY-MM-DD): ")
    ttype = input(f"Enter type for transaction {i+1} (Credit/Debit): ").capitalize()
    amount = int(input(f"Enter amount for transaction {i+1}: "))
    
    transactions.append({"date": date, "type": ttype, "amount": amount})

print("\n----- Bank Statement Report -----")
print("Date        Type      Amount")

total_credit = 0
total_debit = 0
balance = 0

for t in transactions:
    print(f"{t['date']:<12} {t['type']:<8} ₹{t['amount']:>8,}")

    if t["type"] == "Credit":
        total_credit += t["amount"]
        balance += t["amount"]
    else:
        total_debit += t["amount"]
        balance -= t["amount"]
print("---------------------------------")
print(f"{'Total Credit:':<20} ₹{total_credit:,}")
print(f"{'Total Debit:':<20} ₹{total_debit:,}")
print(f"{'Current Balance:':<20} ₹{balance:,}")
print("---------------------------------")

