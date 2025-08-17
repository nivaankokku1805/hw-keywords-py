# Program to calculate the due amount

# Input: Total bill amount
total_amount = float(input("Enter the total bill amount: "))

# Input: Amount paid by the customer
amount_paid = float(input("Enter the amount paid by the customer: "))

# Calculate the due amount
due_amount = total_amount - amount_paid
pass

# Display the result
if due_amount > 0:
    print(f"The customer still owes ₹{due_amount:.2f}.")
elif due_amount < 0:
    print(f"The customer should receive ₹{-due_amount:.2f} as change.")
else:
    print("The bill is fully paid. No amount is due.")