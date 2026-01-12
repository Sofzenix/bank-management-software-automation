from reports import transactions  # import the transactions from reports.py

num_credits = len([t for t in transactions if t['type'] == 'Credit'])
num_debits = len([t for t in transactions if t['type'] == 'Debit'])
largest_credit = max([t['amount'] for t in transactions if t['type'] == 'Credit'], default=0)
largest_debit = max([t['amount'] for t in transactions if t['type'] == 'Debit'], default=0)
avg_transaction = sum(t['amount'] for t in transactions) / len(transactions)

print("\n----- Transaction Analysis -----")
print(f"Number of Credits: {num_credits}")
print(f"Number of Debits: {num_debits}")
print(f"Largest Credit: ₹{largest_credit:,}")
print(f"Largest Debit: ₹{largest_debit:,}")
print(f"Average Transaction Amount: ₹{avg_transaction:,.2f}")
