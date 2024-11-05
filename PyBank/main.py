# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
totalChange = []
months = []


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    firstRow = next(reader)

    total_months += 1 

    previousChange = float(firstRow[1])

    # Extract first row to avoid appending to net_change_list
    for row in reader:
        total_months += 1 
        # Track the total
        total_net += float(row[1])

        # Track net change
        netChange = float(row[1]) - previousChange
        totalChange.append(netChange)

        months.append(row[0])
    
        #update previous revenue
        previousChange = float(row[1])

#calculate averag net change per month
averageChange = sum(totalChange)/total_months

greatestIncrease = ["months[0]", totalChange[0]]
greatestDecrease = ["months[0]", totalChange[0]]

for r in range(len(totalChange)):
    if(totalChange[r] > greatestIncrease[1]):
     
        greatestIncrease[1] = totalChange[r]
        greatestIncrease[0] = months[r]

    if(totalChange[r] < greatestDecrease[1]):
        greatestDecrease[1] = totalChange[r]
        greatestDecrease[0] = months[r]


output = (
    f"\nFinancial Anaylysis \n"
    f"--------------------------\n"
    f"Total Months = {total_months}\n"
    f"Total Revenue = ${total_net}\n"
    f"Average Change  = ${averageChange}\n"
    f"Greatest Increase in Profits  = ${greatestIncrease[0]} Amount ${greatestIncrease[1]}\n"
    f"Greatest Decrease in Profits  = ${greatestDecrease[0]} Amount ${greatestDecrease[1]}\n"
)
    #Print the outputprint(output)
print(output)
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
   txt_file.write(output)
