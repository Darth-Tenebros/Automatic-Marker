

def commission_calculator(percentage, amount):
    return  amount * (percentage/100)

def main():
    amount = eval(input("What is the total amount?\n"))
    percentage = eval(input("What is the percentage of commission policy? [%]\n"))
    print("The total commission is: R{:,.2f}".format(commission_calculator(percentage, amount)))

if __name__ == '__main__':
    main()