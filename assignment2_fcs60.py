print("Nabiha's Salary")

months = ["january","february","march","april","may","june","july",
"august","september","october","november","december"]

month_sal = int(input("Enter the salary of the month in $: "))
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