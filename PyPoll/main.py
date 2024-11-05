# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
votes = [] # list that holds the votes
nameVotes = {}
winningCount = 0 
winningVotes = ""



# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1

        if row[2] not in votes:
            votes.append(row[2])
            nameVotes[row[2]] = 1
        
        else:
            nameVotes[row[2]] += 1
#print(nameVotes)
voter_output = ""

for nameVote in nameVotes:
    votes = nameVotes[nameVote]
    votePct = (float(votes) / float(total_votes)) * 100.00 

    voter_output += f"{nameVote}: {votePct: .2f}% \n"
    #print(voter_output)

    if votes > winningCount:
        winningCount = votes
        winningVotes = nameVote 

winningVoteOutput = f"winner: {winningVotes}"        


output = (
     f"\n\n Election Results\n"
     f"-------------------------\n"
     f"Total Votes: {total_votes:,}\n"
     f"-------------------------\n"
     f"{voter_output}\n"
     f"-------------------------\n"
     f"{winningVoteOutput}\n"
     f"-------------------------\n"
        )

print(output)



with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


  