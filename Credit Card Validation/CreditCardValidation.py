#Program to perform Credit Card validation
#Programmed by Dhivya Udaya Kumar

print("\nWelcome to Credit Card validation programming")
print("\n")

#Function to identify the card type
def cardType(number):
    if(number[0] == '4'):
        return "Visa"
    elif(number[0] == '5'):
        return "MasterCard"
    elif(number[:2] == '37'):
        return "American Express"
    elif(number[0] == '6'):
        return "Discover"
    else:
        return "Invalid"

#Function to validate number of digits in the card
def isValid(number):
    count = 0
    curr = number
    while curr != '':
        digit = curr[len(curr) - 1] #to get final character
        curr = curr[:len(curr) - 1] #to trim last character off the string
        if not digit.isdigit(): #check if non-digits are included
            print("Invalid credit card details")
            return False
        count += 1
    if((count == 13 or count == 14 or count == 15 or count == 16) and (cardType(number) != 'Invalid')):
        return True
    return False

#Function to find if number is single digit, else return the sum of 2 digits
def getDigit(number):
    curr = str(number)
    if len(curr) == 1:
        return curr
    else:
        return int(curr[len(curr) - 1]) + int(curr[len(curr) - 2])

#Function to get sum of double of digit in even place from right to left
def sumOfDoubleEvenPlace(number):
    sum = 0
    curr = number
    while curr != '':
        digit = curr[len(curr) - 2]
        curr = curr[:len(curr) - 2]
        doubleOfDigit = int(digit) * 2
        sum += int(getDigit(doubleOfDigit))
    return sum

#Function to get sum of digits in odd place from right to left
def sumOfOddPlace(number):
    sum = 0
    curr = number
    sum += int(curr[len(curr) - 1])
    curr = curr[:len(curr) - 1]
    while len(curr) > 1:
        digit = curr[len(curr) - 2]
        curr = curr[:len(curr) - 2]
        sum += int(digit)
    return sum

cardNumber = 0

#Credit Card number input
while True:
    cardNumber = input("Enter card number: ")
    isValidCard = isValid(cardNumber)
    if isValidCard == False:
        print("Please enter a valid credit card number")
    else:
       break

#Check for card number validity and print result
if((sumOfDoubleEvenPlace(cardNumber) + sumOfOddPlace(cardNumber)) % 10 == 0):
    print("The card number "+cardNumber+" is a valid "+cardType(cardNumber)+" credit card")
else:
    print("The card number "+cardNumber+" is invalid.")

print("\n")
print("Programmed by Dhivya Udaya Kumar")




