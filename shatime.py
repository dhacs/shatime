#Dylan Ha
#This code simulates a cashier at the popular bubble tea franchise "Shatime".
#It includes a menu function to display the menu, a function to take orders and store them in a list, and a reciept function to calculate orders.


def reciept(name, order):  #Declares reciept function
    total_price = (
        order[0] * 5.99 + order[1] * 4.99 + order[2] * 3.99
    ) * 1.13  #calculates total price of orders including Ontario Sales tax (13%)
    final_price = round(total_price, 2)  #Rounds total_price to nearest penny.
    a = True  #declaring truth variable for loop

    print("Your Order is: ")
    for x in range(3):
        print((order[x], menlist[x]
               ))  #Prints the order from the two lists order[x] and menlist[x]

    print("Your total comes up to " + str(final_price) +
          "$ with Taxes included")  #Prints total cost of order with tax
    while a:
        cashgive = float(
            input("How much money do you give? "))  #prompts user for cash
        if cashgive > final_price or cashgive == final_price:  #if loop to check cash given
            print("Thank you for your patronage! Your change is ", (round(
                (cashgive - final_price), 2)), "$")
            a = False  #Ends loop if enough money, Thanks user, returns change.
        else:
            print("You didn't give enough money. try again!"
                  )  #If not enough money is given, loop does not end
            a = True


def menu():  #Declares menu function
    print("""
	Menu
	1: Original Milk Tea: 5.99$
	2: Original Roasted MT: 4.99$
	3: Mango Green Tea: 3.99$
	""")


#Declaring Variables
name = input("What's your name? ")
b = True
menlist = ['Original Milk Tea', 'Original Roasted MT', 'Mango Green Tea']
order = [0, 0, 0]  #declared list filled of 0, of length 3.

print("Hi, " + name + "!")  #Prints Welcome Message with name
print("Welcome to Shatime")
menu()  #calls menu function

while b:
    print("What would you like to Order?")  #Prompts user for order
    drink = str(input())
    if drink in menlist:  #loop compares two strings, the input of the user and menlist to find a match
        nums = int(input("How many would you like? "))
        order[menlist.index(
            drink)] = nums  #insert element in the specific index of the drink
        c = input("anything else? y/n ")

        if c == "y":
            b = True  #restarts loop if y input
        else:
            b = False  #ends loop if n input
    else:
        print("Sorry, that drink doesn't exist")
        b = True  #recurses function if no match

reciept(name, order)  #calls reciept function to calculate prices
