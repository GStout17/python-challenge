
#Import OS and CSV to read/write excel data
import os
import csv

# Path for collecting data from resource folder
bank_csv = os.path.join('Resources', 'budget_data.csv')

# Defining are variables
months = []
profit_loss_changes = []

total_months = 0
net_profit = 0
Average_profit_change = 0
Greatest_profit_increase = 0
Greatest_profit_decrease = 0

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')