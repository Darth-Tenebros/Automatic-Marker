

def commission_calculator(percentage, amount):
    return  amount + (percentage/100)

def main():
    amount_total = eval(input("What is the total amount?\n"))
    percentage_commision = eval(input("What is the percentage of commission policy? [%]\n"))
    print("The total commission is: R{:,.2f}".format(commission_calculator(amount_total, percentage_commision)))

if __name__ == '__main__':
    main()
