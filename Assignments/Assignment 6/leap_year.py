def leap_year(year):
    # Write your code here. 
    if years % 4 == 0 and year % 100 != 0:
        print(years, "is a Leap Year!")
    elif years % 100 == 0:
        print(years, "is not a Leap Year.")
    elif years % 400 == 0:
        print(years, "is a Leap Year!")
    else:
        print(years, "is not a Leap Year")


if __name__ == "__main__":
    years = [2000, 1994, 1912, 3002, 1700, 1400]
    answers = []
    for year in years:
        answers.append(leap_year(year))
    
    print(answers)