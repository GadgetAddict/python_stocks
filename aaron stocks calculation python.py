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

def profitOrLoss(stockPrice, salePrice):
    if stockPrice > salePrice:
        return false
    else:
        return true
    
stockName = input("Enter the name of the stock:\n")                  
stockQuantity = int(input(f"How many {stockName} stocks would you like to purchase?\n"))
stockPrice = int(input("What is the purchase price for each stock?\n"))
subtotal = stockSubtotal(stockQuantity,stockPrice)

print(f"The Subtotal is ${subtotal}")
print(f"A 2% Commission Fee will be applied (${commissionFee(subtotal):.2f})\n")

totalPurchase = (commissionFee(subtotal)) + subtotal
print(f"The Total Purchase Price is ${totalPurchase:.2f}\n")

print(f"Congratulations! You own {stockName} stock!\n")
print("____________________________________\n")
print("Time to sell All your stocks!\n")

salePrice = int(input("Enter the price per share sold.\n"))
subtotal = stockSubtotal(stockQuantity,salePrice)

print(f"Your Sale of {stockQuantity} {stockName} stock's minus the 2% Fee (${commissionFee(subtotal):.2f}):")
print(f"Is: ${(stockSubtotal(salePrice,stockQuantity))-(commissionFee(subtotal)):.2f}")

if profitOrLoss(stockPrice,salePrice):
    print("You earned a profit")
else:
    print("You lost money")

        





 
