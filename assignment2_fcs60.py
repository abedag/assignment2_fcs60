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
inp_savings = int(input("Savings:"))
inp_rent = int(input("Rent:"))
inp_electricity = int(input("Electricity:"))

savings = float((inp_savings / 100) * month_sal)
rent = float((inp_rent / 100) * month_sal)
electricity = float((inp_electricity / 100) * month_sal)

total_paym = savings + rent + electricity
sal_remainder = month_sal - total_paym 
year_rent_elec = (rent + electricity) * len(months)
sal_squared = month_sal ** 2

add_savings = float(input("Enter the additional savings if exist(in $) if not enter 0: "))

if savings != 0:
    add_result = add_savings / savings
    add_remainder = add_savings % savings
else:
    add_result = 0
    add_remainder = 0

print(f"\n---Financial Summary for {month_name}---")
print(f"Salary: {month_sal}$")
print(f"Savings: {savings}$ --> {inp_savings}%")
print(f"Rent: {rent}$ --> {inp_rent}%")
print(f"Electricity: {electricity}$ --> {inp_electricity}%")
print(f"Total payment: {total_paym}$")
print(f"Remainder: {sal_remainder}$")
print(f"Yearly payments(Rent & Electricity): {year_rent_elec}$")
print(f"Salary squared: {sal_squared}$ (Just for fun)")
print(f"The division of {add_savings}$ by {add_remainder}$ is: {add_result}")
print(f"Remainder after division:{add_remainder}$")
print("---Salary Covered---\n")