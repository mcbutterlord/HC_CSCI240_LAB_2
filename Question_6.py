totalChange = int(input("Enter total change: "))
quarters = totalChange/25
totalChange1 = totalChange - (int(quarters)*25)
dimes = totalChange1/10
totalChange2 = totalChange1 - (int(dimes)*10)
nickels = totalChange2/5
totalChange3 = totalChange2 - (int(nickels)*5)
pennies = totalChange3
print("Quarters:",(int(quarters)))
print("Dimes:",(int(dimes)))
print("Nickels:",(int(nickels)))
print("Pennies:",totalChange3)