# Python Assignment - Calculate Stock prices

# 1. ask the user to enter the name of the stock purchased,number of shares, and the price per share
# 2. assume the buyer pays 2% of the amount for commission
# 3. assume that the buyer sold all stocks. Ask the user to enter the price per share sold.
# 4. assume the buyer will pay another 2% of the amount

#ASSUMPTION: the teacher wants to know the output of the math.

def commissionFee(dollarAmount):
    return dollarAmount * 0.02

def stockSubtotal(qty, price):
    return qty*price

def profitOrLoss(qty, stockPrice, salePrice):
    if stockPrice > salePrice:
        loss = (salePrice - stockPrice) * qty
        return f"You lost {loss:.2f} dollars."
    else:
        profit = (salePrice - stockPrice) * qty
        return f"You earned a {profit:.2f} profit."

    
def getNumberInput(prompt):
    while True:
        print(prompt)
        returnedNumber = input()
        try:
            returnedNumber = float(returnedNumber)
            return returnedNumber
        except:
            print('Please use whole numbers.')
            continue
        if returnedNumber < 1:
            print('Please enter a positive number.')
            continue
        break



   
stockName = input("Enter the name of the stock:\n")
stockQuantity = int(getNumberInput(f"How many {stockName.upper()} stocks would you like to purchase?"))
#stockQuantity = int(input(f"How many {stockName} stocks would you like to purchase?\n"))
stockPrice = getNumberInput("What is the purchase price for each stock?")
#stockPrice = int(input("What is the purchase price for each stock?\n"))

subtotal = stockSubtotal(stockQuantity,stockPrice)
print("____________________________________\n")
print("Stock Purchase Details:")
print(f"{stockQuantity} {stockName} stocks - ${stockPrice} each")
print(f"Subtotal: ${subtotal:.2f}\n")

print(f"A 2% Commission Fee will be applied (${commissionFee(subtotal):.2f})\n")
totalPurchase = (commissionFee(subtotal)) + subtotal
print(f"The Total Purchase Price is ${totalPurchase:.2f}\n")

print(f"Congratulations! You own {stockName.upper()} stock!")
print("____________________________________\n")
print(f"It's time to sell All your {stockName.upper()} stocks!\n")

salePrice = getNumberInput("Enter the price per share sold:")
#salePrice = int(input("Enter the price per share sold.\n"))
subtotal = stockSubtotal(stockQuantity,salePrice)

print(f"The Subtotal is ${subtotal}")
print(f"A 2% Commission Fee will be applied (${commissionFee(subtotal):.2f})\n")
print(f"Your Total is: ${(stockSubtotal(salePrice,stockQuantity))-(commissionFee(subtotal)):.2f}")
#profitAmount = profitOrLoss()

print(profitOrLoss(stockQuantity,stockPrice,salePrice))


#
#    print("You earned a profit")
#else:
#    print("You lost money")

        





 
