"""
this function will calculate and print a receipt for a purchase of coffee and muffins in a campus cafe
the user will tell you how may coffees, muffins, and what percent tip
tax is 8.875%

pseudocode:
    1. call my function campus_cafe
    2. in function campus_cafe:
        A. display menu
            coffees = 2.25
            muffins = 2.75
        B. ask the user how many coffees, how many muffins, and what percent tip
        C. convert coffees and muffins to integer, store these values as coffee_quantity and muffin_quantitiy
        D. add in tr/except in case wrong values are entered
        E. convert tip to float, multiply by .10, store this value as tip
        F. calculate the cost of this cafe order
            coffee_cost= float(coffee_quantity) * 2.25
            muffin_cost= float(muffin_quantity) * 2.75
            subtotal_cost= coffee_cost + muffin_cost
            tax_cost= subtotal_cost * .08875
            tip_cost= subtotal_cost * tip
            total_cost= subtotal_cost + tax_cost + tip_cost
        G. format coffee_cost, muffin_cost, subtotal_cost, tax_cost, tip_cost, and total_cost to two decimal places
        H. print formatted receipt
           --- receipt ---
            coffe_quantity "* Coffee @ $2.25 =" coffee_cost
            muffin_quantity "* Muffin @ $2.75 =" muffin_cost
            "Subtotal=" subtotal_cost
            "Tax (8.875%) =" tax_cost
            f"Tip{tip} = {tip_cost}"
            "TOTAL =" total_cost
            "Thank you for your business!"

"""

#print menu
def campus_cafe():
    print ("============================== \n Welcome to Campus Cafe! \n ===Menu=== \n Coffee = $2.25 \n Muffin = $2.75 \n ==============================")

#collect user input: number of coffees, number of muffins, and tip
def user_input():
    import sys
    question1= "how many coffees?"
    question2= "how many muffins?"
    question3= "enter tip percent(e.g. 10 for 10%)"

    # prepare in case the wrong vlaue is entered

    try:
        coffee_quantity = int(input(question1))
        muffin_quantity = int(input(question2))
        tip = int(input(question3))

        if (not(coffee_quantity >= 0)) or (not(muffin_quantity >= 0)) or (not(tip >= 0)):
            raise ValueError

        # calculate costs
        tip_percent= float(tip) /100 #converts the tip percent into a usable decimal
        coffee_cost= float(coffee_quantity) * 2.25  #calculates the cost of coffee
        muffin_cost= float(muffin_quantity) * 2.75  #calculate the cost of muffins
        subtotal_cost= coffee_cost + muffin_cost    #calculates the subtotal cost
        tax_cost= subtotal_cost * .08875    #calculates the cost of tax
        tip_cost= subtotal_cost * tip_percent   #calculates the tip cost

        #convert to currency format
        coffee_receipt= f"{coffee_cost:,.2f}"   #converts the cost of coffee into currency format
        muffin_receipt= f"{muffin_cost:,.2f}"   #converts the cost of muffins into currency format
        subtotal_receipt= f"{subtotal_cost:,.2f}"   #converts the subtotal cost into currency format
        tax_receipt= f"{tax_cost:,.2f}"     #converts the subtotal cost into currency format
        tip_receipt= f"{tip_cost:,.2f}"     ##converts the tip cost into currency format
        total_cost= f"{subtotal_cost + tax_cost + tip_cost:,.2f}"   #calculates the total cost and converts it to currency format

    #prepare error code
    except ValueError:
        print("Invalid number. Goodbye!")
        sys.exit(1)

    #print receipt
    print(f"------------------------------- \n ---Receipt--- \n {coffee_quantity} x Coffee @ $2.25 = ${coffee_receipt} \n {muffin_quantity} x Muffin @ $2.75= ${muffin_receipt} \n Tax(8.875%)= ${tax_receipt} \n Tip= ${tip_receipt} \n TOTAL= ${total_cost} \n Thank you for your business! \n ------------------------------")

#define the main function
def main():
    campus_cafe()
    user_input()

#call the function
if __name__=="__main__":
  main()
    




