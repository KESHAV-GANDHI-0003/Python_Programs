#Read the limit
limit = float(input("Enter the limit"))
max_price = 0
# Read the next price
next_price = float(input("Enter a price or 0 to stop:"))
while next_price > 0 :
    if next_price < limit and next_price > max_price:
        max_price = next_price
    #Read the next price
    next_price = float(input("Enter a price or 0 to stop:"))
if max_price > 0:
    print("Largest Price =", max_price)
else :
    print("Prices exceed limit of", limit);