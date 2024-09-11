print("Rental Car Fee")
days = int(input("Enter days rented: "))
miles = int(input("Enter miles driven: "))
#Total Fee is $49.50 for each day rented plus $.09 per mile
totalCost = ((days*49.50)+(miles*.09))
print("Total Fee:",totalCost)