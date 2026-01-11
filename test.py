# sudoku


def income_tax(income):

    if income >= 400000 and income <= 800000:
        tax = (income * 5) / 100
        print("Tax for income is :", tax)
    else:
        if income > 800000 and income <= 1200000:
            tax = (income * 10) / 100
            print("Tax for income is :", tax)
        else:
            if income > 1200000 and income <= 1600000:
                tax = (income * 15) / 100
                print("Tax for income is :", tax)
            else:
                if income > 1600000 and income <= 2000000:
                    tax = (income * 20) / 100
                    print("Tax for income is :", tax)
                else:
                    if income > 2000000 and income <= 2400000:
                        tax = (income * 25) / 100
                        print("Tax for income is :", tax)
                    else:
                        if income > 2400000:
                            tax = (income * 30) / 100
                            print("Tax for income is :", tax)
                        else:
                            print("Tax for income is null")


income_tax(100000)
