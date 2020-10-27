def leap_year(year):
    # Write your code here. 
    year = int(input("Enter the year:" ))

if __name__ == "__main__":
    years = [2000, 1994, 1912, 3002, 1700, 1400]
    answers = []
    for year in years:
        answers.append(leap_year(year))
    
    print(answers)