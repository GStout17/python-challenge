

# Import dependencies
import os
import csv
import collections
from collections import Counter

# Defining our variables
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

    # finding the percentage of votes per candicate (three digit places! '.3f')
    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')

# Print the voting analysis, don't forget f string & {}
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


