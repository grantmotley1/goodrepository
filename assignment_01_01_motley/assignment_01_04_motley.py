# Grant Motley
# CBIS 4210
# Assignment 1.1
# 9/27/2024

# calculate the total price after applying a discount
def main():
    # get the price of the item
    price = float(input("Enter the price of the item: "))
    # get the discount rate
    discount_rate = float(input("Enter the discount rate: "))

    # calculate the discount
    discount = price * discount_rate / 100
    # calculate the total price
    total_price = price - discount

    # print the total price
    print("The total price is $", total_price)

# call the main function
main()
