
#Import OS and CSV to read/write excel data
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
current_month_profit_loss = 0

# Read in the CSV file
with open(bank_csv_path, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the 1st header (column)
    header = next(csvfile)

    # print(f"header: {header}") 

    # Creating loop to read through each row (not including the header)
    for row in csvreader:

        

        # Getting the total months and total net profit
        total_months = total_months +1
        net_profit = net_profit +int(row[1]) 

        # Needed for indexing/calculating greatest & worst profit increase
        date.append(row[0])

        # Finding the profit changes by each month
        profit_changes = int(row[1]) - previous_monthly_profit
        previous_monthly_profit = int(row[1])
        
        # Store profit changes of each month in a list
        monthly_changes.append(profit_changes)

        # Finding the average in profits across the entire time frame (don't forget about rounding!)
        #average_change_profits = round(net_profit/(total_months), 2)
        average_change_profits = sum(monthly_changes) / len(monthly_changes)

        # Finding the greatest increase and decrease in profits
        greatest_increase = max(monthly_changes)
        greatest_decrease = min(monthly_changes)
        
        # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
        highest_month_index = monthly_changes.index(greatest_increase)
        lowest_month_index = monthly_changes.index(greatest_decrease)
        
        # Assing the best and worst date
        best_month = date[highest_month_index]
        worst_month = date[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_profit}")
print(f"Average Change:  ${average_change_profits}")
print(f"Greatest Increase in Profits:  {best_month} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {worst_month} (${greatest_decrease})")



    