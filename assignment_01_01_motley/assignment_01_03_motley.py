# Grant Motley
# CBIS 4210
# Assignment 1.1
# 9/27/2024

# calculate total price including sales tax
def main():
    # get the price of the item
    price = float(input("Enter the price of the item: "))
    # get the sales tax rate
    tax_rate = float(input("Enter the sales tax rate: "))

    # calculate the sales tax
    tax = price * tax_rate / 100
    # calculate the total price
    total_price = price + tax

    # print the total price
    print("The total price is $", total_price)

# call the main function
main()
