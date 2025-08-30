#Input the price
itemprice = float(input("Enter Item price: "))

print("_" * 20)

#This formats the number that you put for price into a two decimal number (Ex. 12.22)
print(f"Item price is: $", format (itemprice, ".2f"))

#Multiplies the number previously entered by tips
print("Tip (15%): $", format (itemprice * 0.15, ".2f"))

#Tip equation
tip = float(itemprice * 0.15)

#Predicts total price
print("Total Price: $", format (itemprice + tip, ".2f"))