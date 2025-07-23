#dotscolumn = int(input("How many x dots you want to print? "))
#dotsrow = int(input("How many y dots do you want to print? "))
#for i in range(dotscolumn):
    #for j in range(dotsrow):
        #print("*", end =" ")
    #print()  # Move to the next line after printing one row of dots
    
#THIS IS FOR ADDING A NEW LINE AFTER EACH ROW WITHOUT USING PRINT⬇️ (Instructor Reuben showed me this) (Also a String Concatenation)
#for i in range(row):  
    #row_string = ""
    #for j in range(column):
         #row_string += "* "
    #row_string += "\n" #Add a newline at the end of each row
    #print(row_string, end="") #Prevents extra blank lines
    
#This code prints a grid of dots based on user input for the number of columns and rows, using a specified symbol.
#print("Loop Grid Challenge!")
#dotscolumn = int(input("How many x dots you want to print? "))
#dotsrow = int(input("How many y dots do you want to print? "))
#symbol = input("What symbol do you want to print? ")
#print(f"Printing {dotscolumn} * {dotsrow} dots with the symbol '{symbol}'")
#for i in range(dotsrow):
    #for j in range(dotscolumn):
        #print(symbol, end=" ")
    #print()  # Move to the next line after printing one row of dots
   
   
    
print("Loop Grid Challenge!")
dotscolumn = int(input("How many x dots you want to print? "))
dotsrow = int(input("How many y dots do you want to print? "))
symbol = input("What symbol do you want to print? ") #Lets the user choose a symbol to print
print(f"Printing {dotscolumn} * {dotsrow} dots with the symbol '{symbol}'") #Multiplying the number of columns and rows by the symbol
for i in range(dotsrow):
    row_string = "" #Initialize an empty string for each row
    for j in range(dotscolumn):
         row_string += (f"{symbol}") #Concatenate the symbol to the row string
    row_string += "\n" #Add a newline at the end of each row
    print(row_string, end="") #Prevents extra blank lines
    
 #///String concatenation is used to build the row string, which is then printed in one go to avoid multiple print calls.\\\#
