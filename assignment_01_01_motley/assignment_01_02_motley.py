# Grant Motley
# CBIS 4210
# Assignment 1.1
# 9/27/2024

# calculate the pay for an employee
def main():
    # get the employee's name
    name = input("Enter the employee's name: ")
    # get the number of hours worked
    hours = float(input("Enter the number of hours worked: "))
    # get the hourly wage
    wage = float(input("Enter the hourly wage: "))

    # calculate the gross salary
    pay = hours * wage

    # print the pay amount
    print(name, "earned $", pay, "this week.")

# call the main function
main()


