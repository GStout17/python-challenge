
#Import OS and CSV to read/write excel data
import os
import csv

# Path for collecting data from resource folder
bank_csv_path = os.path.join('Resources', 'budget_data.csv')

# Defining are variables
months = []
total_net_profit = []
profit_changes = []

total_months = 0
net_profit = 0
previous_monthly_profit= 0
Average_profit_change = 0
Greatest_profit_increase = 0
Greatest_profit_decrease = 0

# Read in the CSV file
with open(bank_csv_path, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the 1st header (column)
    header = next(csvfile)

    print(f"header: {header}")

    # Creating loop to read through each row (not including the header)
    for row in csvreader:

        #Getting the total months and total net profit
        total_months = total_months +1
        net_profit = net_profit +int(row[1]) 

        
        profit_changes = int(row[1]) - previous_monthly_profit
        previous_monthly_profit = int(row[1])
        print(profit_changes)


    