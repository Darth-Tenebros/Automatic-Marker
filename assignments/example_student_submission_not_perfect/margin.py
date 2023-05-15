import vat

def calculate_selling_price_with_VAT(amount, margin, VAT):
    return vat.add_VAT(amount * (1+(margin/100)), VAT)

def get_margin_amount(amount, margin):
    return amount - (amount / (1 + (margin / 100)))

def main():
    amount = eval(input("What is the total amount?\n"))
    margin = eval(input("What is the profit margin to add? [%]\n"))
    VAT_percentage = eval(input("What is the VAT percentage? [%]\n"))
    print("The selling price with tax is: R{:,.2f}".format(calculate_selling_price_with_VAT(amount, margin, VAT_percentage)))


if __name__ == '__main__':
    main()