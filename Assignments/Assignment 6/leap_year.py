def leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year, "is a Leap Year!")
            else:
                print(year, "is not a Leap Year.")
        else:
            print(year, "is a Leap Year!")
    else:
        print(year, "is not a Leap Year.")


if __name__ == "__main__":
    years = [2000, 1994, 1912, 3002, 1700, 1400]
    answers = []
    for year in years:
        answers.append(leap_year(year))
    
    print(answers)