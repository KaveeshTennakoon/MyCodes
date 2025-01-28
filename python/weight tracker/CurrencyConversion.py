def main():

    while True:

        try:
            print("Choose the conversion \n    1. USD to LKR \n    2. LKR to USD\n")
            option = int(input("Enter your option: "))

            if option == 1 or option == 2:
                break
            else:
                print("\nPlease enter enter either '1' or '2'.\n")
        except ValueError:
            print("\nPlease enter a valid integer.\n")

    if option == 1:
        USDtoLKR()
    else:
        LKRtoUSD()

def USDtoLKR():
        
    while True:

        try:

            usd = float(input("\nEnter the amount in USD: $"))
            if usd >= 0:
                break
            else:
                print("Amount must not be negative") 

        except ValueError:
            print("Enter a valid amount.")

    lkr = usd * 320

    print("Your amount in LKR is Rs.", lkr, sep="")

def LKRtoUSD():
        
    while True:

        try:

            usd = float(input("\nEnter the amount in LKR: Rs"))
            if usd >= 0:
                break
            else:
                print("Amount must not be negative") 

        except ValueError:
            print("Enter a valid amount.")

    lkr = usd * 320

    print("Your amount in LKR is $", lkr, sep="")

if __name__ == "__main__":
    main()