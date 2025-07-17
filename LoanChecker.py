#Print a welcome message
print("Welcome to Mojojo Loan Checker")

#Start an infinite loop so the user can reapply if they want
while True:
    #Get user's age, income, loan amount and product details
    age = int(input("Enter your age: "))
    income = float(input("Enter your monthly income: "))
    loan_amount = float(input("Enter desired loan amount: "))
    product = input("What loan product do you want? (business loan, salary advance, SME loan  ): ").lower()

#Check eligibility conditions
    if age < 21:
        print("Sorry, you must be at least 21 to apply")
    elif income < 30000:
        print("Your income is below the minimum required for a loan")
    elif loan_amount > income * 5:
        print("We cannot give loans more than 5X your income.")
    elif product not in ["business loan" , "salary advance", "SME loan"]:
        print("Sorry, that loan product is not supported")
    else:
        print("You are eligible for a loan! We'll contact you soon.")

#Additional note for younger applicants
    if age < 25:
        print("Note: Young borrowers may need a guarantor.")

#Ask if the user wants to apply again
    new = input("Would you like to apply again? (yes/no: )").lower()
    if new != "yes":
        print("Thank you for using Mojojo Loan Checker. Bye!")
        break #Exit the loop if the user doesn't want to apply again