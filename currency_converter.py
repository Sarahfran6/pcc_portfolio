def usd_to_eur(amount):
    return amount *0.9

def eur_to_usd(amount):
    return amount / 0.9

def usd_to_gbp(amount):
    return amount / 0.8

def gbp_to_usd(amount):
    return amount / 0.8

def usd_to_ngn(amount):
    return amount / 1600

def ngn_to_usd(amount):
    return amount /1600

def main():
    print("Welcome to currency converter\nEnter the followung number for your conversion")
    print("1. USD to EUR")
    print("2. EUR to USD")
    print("3. USD to GBP")
    print("4. GBP to USD")
    print("5. USD to NGN")
    print("6. NGN to USD")

choice = int(input("Enter your chioce: "))

amount = float(input("Enter the amount: "))


if choice == 1:
    print("${} is €{}".format(amount, usd_to_eur(amount)))
elif choice == 2:
    print("€{} is ${}".format(amount, eur_to_usd(amount)))
elif choice == 3:
    print("${} is £{}".format(amount, usd_to_gbp(amount)))
elif choice == 4:
    print("£{} is ${}".format(amount, gbp_to_usd(amount)))
elif choice == 5:
    print("${} is N{}".format(amount, usd_to_ngn(amount)))
elif choice == 6:
    print("N{} is ${}".format(amount, ngn_to_usd(amount)))
else:
    print ("invalid choice")






