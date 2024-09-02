# Grant Motley
# CBIS 4210
# Assignment 1.1
# 9/27/2024

# calculate simple interest
def main():
    # get the principle
    principle = float(input("Enter the principle amount: "))
    # get the interest rate
    rate = float(input("Enter the interest rate: "))
    # get the time period in years
    time = float(input("Enter the time period (in years): "))
    # calculate the interest
    interest = (principle * rate * time) / 100
    # print the interest
    print("The interest gained is $", interest)

# call the main function
main()



