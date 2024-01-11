# the program will ask user to enter custom parameters.

# Create an Array
customer = []

# Recursively ask user to enter by creating a loop
while True:

    # Get input from users and make it why for Y or N 
    createEntry = input(" Enter Customer (Y / N): ")
    createEntry = createEntry[0].lower()
    
    #Check to leave loop
    if createEntry == "n":
        break

    # Get customer data
    else:
        fname, lname = input("Enter Customer Name:  ").split()
    # Add customer data 
    customer.append({'fname': fname, 'lname': lname})


# print out customer data
for cust in customer:
    print(cust['fname'], cust['lname'])