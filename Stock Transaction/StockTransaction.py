#Program to perform stock transaction calculations
#Programmed by Dhivya Udaya Kumar

print("Welcome to stock transaction programming")
print("\n")

#Inputs for purchasing shares
customerName = input("Enter name of person: ")

while True:
    try:
        numOfSharesBought = int(input("Enter the number of shares purchased by " + customerName + ": "))
        assert(numOfSharesBought > 0), 'Number must be greater than 0'
        break
    except:
        print("Please enter a valid number")

while True:
     try:
        pricePerShareBought = float(input("Enter the price per share: $"))
        assert(pricePerShareBought > 0), 'Price must be greater than 0'
        break
     except:
        print("Please enter a valid price")

while True:
    try:
        commissionPercentageWhileBuying = float(input("Enter the percentage of commission given to the stock broker: "))
        assert (commissionPercentageWhileBuying > 0), 'Commission percentage must be greater than 0'
        break
    except:
        print("Please enter a valid commission percentage")

print("")

#Shares purchase calculations
totalShareBuyingPrice = numOfSharesBought * pricePerShareBought
print("Amount of money paid for the stock = $", totalShareBuyingPrice)
totalCommissionWhileBuying = totalShareBuyingPrice * commissionPercentageWhileBuying / 100
print("Amount of commission paid to stock broker while buying stock = $",totalCommissionWhileBuying)
print("\n")

#Inputs for selling shares
while True:
    try:
        numOfSharesSold = int(input("Enter the number of shares sold by " + customerName + ": "))
        assert (numOfSharesBought > 0), 'Number must be greater than 0'
        break
    except:
        print("Please enter a valid number")

while True:
    try:
        pricePerShareSold = float(input("Enter the price per share: $"))
        assert (numOfSharesBought > 0), 'Price must be greater than 0'
        break
    except:
        print("Please enter a valid price")

while True:
    try:
        commissionPercentageWhileSelling = float(input("Enter the percentage of commission given to stock broker: "))
        assert (numOfSharesBought > 0), 'Commission percentage must be greater than 0'
        break
    except:
        print("Please enter a valid commission percentage")

print("")

#Shares selling calculations
totalShareSellingPrice = numOfSharesSold * pricePerShareSold
print("Amount for while stock is sold = $", totalShareSellingPrice)
totalCommissionWhileSelling = totalShareSellingPrice * commissionPercentageWhileSelling / 100
print("Amount of commission paid to stock broker while selling stock = $", totalCommissionWhileSelling)
amountRemaining = (totalShareSellingPrice - totalCommissionWhileSelling) - (totalShareBuyingPrice + totalCommissionWhileBuying)
print("Amount of money ($) left with " + customerName + " after selling stock and paying commissions at both times = ", amountRemaining)
print("")

if amountRemaining < 0:
    print(customerName + " lost money!")
elif amountRemaining == 0:
    print(customerName + " neither made a profit nor loss!")
else:
    print(customerName + " made a profit!")

print("\n")
print("Programmed by Dhivya Udaya Kumar")