# Function to calculate due amount
def calculate_due_amount(total_amount, amount_paid):
    # Calculate the due amount by subtracting the amount paid from the total amount
    due_amount = total_amount - amount_paid
    return due_amount

# Main program execution
if __name__ == "__main__":
    try:
        # Get user input for total amount and amount paid
        total_amount = float(input("Enter the total bill amount: "))
        amount_paid = float(input("Enter the amount paid by the customer: "))
        
        # Calculate the due amount
        due = calculate_due_amount(total_amount=total_amount, amount_paid=amount_paid)
        
        # Check if there is any due amount
        if due > 0:
            print(f"The due amount is: {due}")
        elif due == 0:
            print("The bill is fully paid. No due amount.")
        else:
            print(f"Overpayment! Refund the customer: {-due}")
    
    except ValueError:
        # Handle invalid input (non-numeric values)
        print("Invalid input. Please enter valid numeric values for the amount.")