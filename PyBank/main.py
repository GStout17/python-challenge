
#Import OS and CSV to read/write excel data (dependancies)
import os
import csv

# Path for collecting data from resource folder
bank_csv_path = os.path.join('Resources', 'budget_data.csv')

# Defining are variables
monthly_changes = []
date = []

total_months = 0
net_profit = 0
profit_changes = 0
previous_monthly_profit= 0
current_month_profit = 0

# Read in the CSV file
with open(bank_csv_path, newline="") as csvfile:

    # Split the data via commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the 1st header (column)
    header = next(csvfile)

    # Creating loop to read through each row (not including the header)
    for row in csvreader:


        # Getting the total months and total net profit
        total_months = total_months +1
        current_month_profit = int(row[1])
        net_profit += current_month_profit

        # This allows for the correct average change by making the previous month equal to the current month
        if (total_months ==1):
            previous_monthly_profit = current_month_profit
            continue

        # Needed for indexing/calculating greatest & worst profit increase
        date.append(row[0])

        # Finding the profit changes by each month
        profit_changes = int(row[1]) - previous_monthly_profit
        previous_monthly_profit = int(row[1])
        
        # Store profit changes of each month in a list
        monthly_changes.append(profit_changes)

        # Finding the average in profits across the entire time frame (don't forget about rounding!)
        average_change_profits = round((sum(monthly_changes) / len(monthly_changes)), 2)

        # Finding the greatest increase and decrease in profits
        greatest_increase = max(monthly_changes)
        greatest_decrease = min(monthly_changes)
        
        # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
        highest_month_index = monthly_changes.index(greatest_increase)
        lowest_month_index = monthly_changes.index(greatest_decrease)
        
        # Assing the best and worst date
        best_date = date[highest_month_index]
        worst_date = date[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_profit}")
print(f"Average Change:  ${average_change_profits}")
print(f"Greatest Increase in Profits:  {best_date} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {worst_date} (${greatest_decrease})")



    