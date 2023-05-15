

def add_VAT(amount, percentage):
    return amount * (1+(percentage/100))

def subtract_VAT(amount, percentage):
    return amount / (1+(percentage/100))

def main():

    choice = input("What would you like to do? [1 or 2]\n"
                   "1 - Add VAT\n"
                   "2 - Subtract VAT\n")
    amount = eval(input("What is the total amount?\n"))
    percentage = eval(input("What is the percentage of VAT? [%]\n"))
    if choice == "1":
        print("The total amount with VAT is: R{:,.2f}".format(add_VAT(amount, percentage)))
    elif choice == "2":
        print("The total amount with VAT is: R{:,.2f}".format(subtract_VAT(amount, percentage)))



if __name__ == '__main__':
    main()