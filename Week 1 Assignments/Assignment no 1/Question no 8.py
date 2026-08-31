# Calculate Profit or Loss 
# Input cost price and selling price. Display either: 
# Profit and amount, or 
# Loss and amount, or 
# No Profit No Loss

cost_price = float(input("Enter cost price: "))

selling_price = float(input("Enter selling price: "))

if cost_price == selling_price:
    print("No Profit No Loss")

elif cost_price < selling_price:
    print(f"Profit {selling_price - cost_price}")

else:
    print(f"Loss {cost_price - selling_price}")