
#Import OS and CSV to read/write excel data
import os
import csv

# Path for collecting data from resource folder
bank_csv_path = os.path.join('Resources', 'budget_data.csv')

# Defining are variables
months = []
total_net_profit = []
monthly_changes = []


total_months = 0
net_profit = 0
profit_changes = 0
previous_monthly_profit= 0
Average_profit_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]


# Read in the CSV file
with open(bank_csv_path, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the 1st header (column)
    header = next(csvfile)

    print(f"header: {header}")

    # Creating loop to read through each row (not including the header)
    for row in csvreader:

        # Getting the total months and total net profit
        total_months = total_months +1
        net_profit = net_profit +int(row[1]) 

        # Finding the profit changes by each month
        profit_changes = int(row[1]) - previous_monthly_profit
        previous_monthly_profit = int(row[1])
        
        # Store profit changes of each month in a list
        monthly_changes.append(profit_changes)

        # Finding the average in profits
        average_change_profits = (net_profit/total_months)
        print(average_change_profits)
        #profit_changes.append(int(row[1]))

        # Finding the greatest increase and decrease in profits
        


        #if profit_changes = int(row[1])


    