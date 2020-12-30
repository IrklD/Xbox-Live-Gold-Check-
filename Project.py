"""
Check if user has xbox gold if not offer him to buy it,
if user below 18 do not allow to buy and tell him to wait _ more years
"""

import datetime as dt

date = dt.datetime.now()
year = str(date.year)
yeardate = list(year)
current_year = int(yeardate[2] + yeardate[3])
# #################################################################################################################
class Xbox_Gold:
    def __init__(self, name, age, membership):
        self.name = name
        self.age = age
        self.membership = membership

class Xbox_Gold_Check:
    def __init__(self, name_check):
        self.name_check = name_check
# #################################################################################################################
try:
    # list of users with xbox gold they will be entered by the system for now its just useless with some nicks for testing
    gold_users = ["Denis", "George"]
    print("Xbox Live Gold Website\n")
    xbox_user = Xbox_Gold(input("Enter username: "), int(input("Enter age: ")), input("Enter membership status: "))

    if xbox_user.name in gold_users:
        print("This user already has xbox live gold")
        exit()
    else:
        pass

    if xbox_user.age > 99:
        print("Enter proper age from 18 to 99")
        exit()

    elif xbox_user.membership.lower() == "gold":
        print(xbox_user.name + " with gold you got access to a new game for free each month and multiplayer")
        exit()

    elif xbox_user.membership.lower() == "none":
        print("\nIn order to get access to a new game for free each month and multiplayer you should consider purchasing Xbox Live Gold\n")
        purchase = input("Do you want to buy Xbox Live Gold - 12 months for 55$?\ny/n?")


    else:
        print(xbox_user.name + " enter valid membership status if you don't have one type none\n")
        exit()

    def checking_user():
        xbox_user1 = Xbox_Gold(input("Enter username: "), int(input("Enter age: ")), input("Enter membership status: "))
        if xbox_user1.name == xbox_user.name or xbox_user1.name in gold_users:
            print("\nUser already has xbox live gold!")
        elif xbox_user1.age > 99:
            print("\nEnter proper age from 18 yo 99")
            exit()
        elif xbox_user1.membership.lower() == "gold":
            print(xbox_user1.name + " with gold you got access to a new game for free each month and multiplayer")
            exit()

        elif xbox_user1.membership.lower() == "none":
            print("\nIn order to get access to a new game for free each month and multiplayer you should consider purchasing Xbox Live Gold\n")
            purchase1 = input("Do you want to buy Xbox Live Gold - 12 months for 55$?\ny/n?")
            if purchase1.lower() == "y" or purchase1.lower() == "yes":
                credit_card = int(input("\nEnter credit card number: "))
                if len(str(credit_card)) < 13 or len(str(credit_card)) > 19:
                    print("\nEnter valid credit card length between 13 and 19\n")
                    exit(checking_user())
                else:
                    pass


                cvv = int(input("Enter cvv: "))
                if len(str(cvv)) != 3:
                    print("\ncvv number must be 3 characters long! \n")
                    exit(checking_user())
                else:
                    pass


                credit_datemonth = int(input("Enter credit card month expiration date: "))
                if credit_datemonth > 12:
                    print("\nThere are no more months than 12!\n")
                    exit(checking_user())
                elif len(str(credit_datemonth)) > 2:
                    print("\nCan not enter more than 2 characters for a month\n")
                    exit(checking_user())
                else:
                    pass


                credit_dateyear = int(input("Enter credit card year expiration date: "))
                if credit_dateyear < current_year:
                    print("\nCredit card already expired\n")
                    exit(checking_user())
                elif len(str(credit_dateyear)) > 2:
                    print("\nEnter only 2 last digits of current year\n")
                    exit(checking_user())
                else:
                    pass
                print("\nThanks for the purchase 55$ have been transferred from your account\n".title())

            elif purchase1.lower() == "n" or purchase1.lower() == "no":
                print(xbox_user.name + " you have the standard membership with no perks or features :(".title())


    def membership():
        if purchase.lower() == "y" or purchase.lower() == "yes":
            credit_card = int(input("\nEnter credit card number: "))
            if len(str(credit_card)) < 13 or len(str(credit_card)) > 19:
                print("\nEnter valid credit card length between 13 and 19\n")
                exit(membership())
            else:
                pass


            cvv = int(input("Enter cvv: "))
            if len(str(cvv)) != 3:
                print("\ncvv number must be 3 characters long\n")
                exit(membership())
            else:
                pass


            credit_datemonth = int(input("Enter credit card month expiration date: "))
            if credit_datemonth > 12:
                print("\nThere are no more months than 12!\n")
                exit(membership())
            elif len(str(credit_datemonth)) > 2:
                print("\nCan not enter more than 2 characters for a month\n")
                exit(membership())
            else:
                pass


            credit_dateyear = int(input("Enter credit card year expiration date: "))
            if credit_dateyear < current_year:
                print("\nCredit card already expired\n")
                exit(membership())
            elif len(str(credit_dateyear)) > 2:
                print("\nEnter only 2 last digits of current year\n")
                exit(membership())
            else:
                pass
            print("\nThanks for the purchase 55$ have been transferred from your account\n".title())
            print("Checking in user's gold status...".upper())

            xbox_user_check = Xbox_Gold_Check(input("Enter username: "))
            if xbox_user_check.name_check.lower() == xbox_user.name.lower() or xbox_user_check.name_check in gold_users:
                print("\nThis user has an xbox live gold:)")
                exit()

            else:
                print("\nUser doesnt have gold\n")
                print("__RESTARTING PROGRESS__")
                checking_user()

        elif purchase.lower() == "n" or purchase.lower() == "no":
            print(xbox_user.name + " you have the standard membership with no perks or features :(".title())

    membership()

except(ValueError):
    print("Invalid input!")


