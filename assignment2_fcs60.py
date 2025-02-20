print("Nabiha's Salary")

months = ["january","february","march","april","may","june","july",
"august","september","october","november","december"]

while True:
    month_sal = input("Enter the salary of the month in $: ")
    if month_sal.replace(".", "", 1).isdigit():
        salary = float(month_sal)
        break
    else:
        print("Invalid input. Please enter a valid number")

month_name = input("Enter the name of the month: ")

while month_name.lower() not in months:
    print("Month entered doesn't exist. Please Try again")
    month_name = input("Enter the name of the month: ")

print("Enter the percentage of each of the following payments:")

while True:
    inp_savings = input("Savings (Without typing %):")
    if inp_savings.replace(".", "", 1).isdigit():
        savings_percent = float(inp_savings)
        break

while True:
    inp_rent = input("Rent (Without typing %):")
    if inp_rent.replace(".", "", 1).isdigit():
        rent_percent = float(inp_rent)
        break
    else:
        print("Invalid input. Please enter a valid percentage.")

while True:
    inp_electricity = input("Electricity (Without typing %):")  
    if inp_electricity.replace(".", "", 1).isdigit():
        electricity_percent = float(inp_electricity)
        break
    else:
        print("Invalid input. Please enter a valid percentage.")

savings = (savings_percent / 100) * salary
rent = (rent_percent / 100) * salary
electricity = (electricity_percent / 100) * salary

total_paym = savings + rent + electricity
sal_remainder = salary - total_paym 
year_rent_elec = (rent + electricity) * len(months)
sal_squared = salary ** 2


while True:
    add_savings = input("Enter the additional savings if exist(in $) if not enter 0: ")
    if add_savings.replace(".", "", 1).isdigit():
        a_savings = float(add_savings)
        break


if savings != 0:
    add_result = a_savings / savings
    add_remainder = a_savings % savings
else:
    add_result = 0
    add_remainder = 0

print(f"\n---Financial Summary for {month_name}---")
print(f"Salary: {salary:.2f}$")
print(f"Savings: {savings:.2f}$ --> {savings_percent:.2f}%")
print(f"Rent: {rent:.2f}$ --> {rent_percent:.2f}%")
print(f"Electricity: {electricity:.2f}$ --> {electricity_percent:.2f}%")
print(f"Total payment: {total_paym:.2f}$")
print(f"Remainder: {sal_remainder:.2f}$")
print(f"Yearly payments(Rent & Electricity): {year_rent_elec:.2f}$")
print(f"Salary squared: {sal_squared:.2f}$ (Just for fun)")
print(f"The division of {a_savings:.2f}$ by {add_remainder:.2f}$ is: {add_result:.2f}")
print(f"Remainder after division:{add_remainder:.2f}$")
print("---Salary Covered---\n")