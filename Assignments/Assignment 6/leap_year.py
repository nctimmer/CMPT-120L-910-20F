def leap_year(year):
    # Write your code here. 
    year = int(input("Enter the year:" ))

    if year % 4 == 0 and year % 100 != 0:
        print(year, "is a Leap Year!")
    elif year % 100 == 0:


if __name__ == "__main__":
    years = [2000, 1994, 1912, 3002, 1700, 1400]
    answers = []
    for year in years:
        answers.append(leap_year(year))
    
    print(answers)