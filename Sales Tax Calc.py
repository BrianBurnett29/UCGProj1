#Input the price
itemprice = float(input("Enter Item price: "))

print("_" * 20)

#This formats the number that you put for price into a two decimal number (Ex. 12.22)
print(f"Item price is: $", format (itemprice, ".2f"))

#Multiplies the number previously entered by the Sales Tax
print("Sales Tax: $", format (itemprice * 0.0825, ".2f"))

#Sales Tax equation
salestax = float(itemprice * 0.0825)

#Predicts total price
print("Total Price: $", format (itemprice + salestax, ".2f"))

print("SALES TAX COMPLETE")