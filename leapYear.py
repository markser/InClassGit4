
def calcLeapYear():
    userInputYear = int(input("Enter a year: "))

    if (userInputYear % 4) == 0:
        if (userInputYear % 100) == 0:
            if (userInputYear % 400) == 0:
                print(str(userInputYear) + " is a leap year")
            else:
                print(str(userInputYear) + " is not a leap year")
        else:
            print(str(userInputYear) + " is a leap year")
    else:
        print(str(userInputYear) + " is not a leap year")



def main():
    calcLeapYear()


if __name__ == "__main__":
    main()
