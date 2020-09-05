

# Import dependencies
import os
import csv
import collections
from collections import Counter

# Defining are variables
candidates = []
votes_per_candidate = []

# Path for collecting data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Read in CSV file
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header of the first row
    csv_header = next(csvfile)

    # Creating loop to read through each row (not including the header)
    for row in csv_reader:

        # Appened to store
        candidates.append(row[2])

    # Sorting our list
    sorted_list = sorted(candidates)
    
    # Organize the sorted list by most common outcomes
    ordered_list = sorted_list

    # Count votes per candidate then append to the created list
    count_candidate = Counter (ordered_list) 
    votes_per_candidate.append(count_candidate.most_common())


