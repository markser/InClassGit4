
def calcLeapYear(userInputYear):
    # userInputYear = int(input("Enter a year: "))

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
    calcLeapYear(2020)


if __name__ == "__main__":
    main()
