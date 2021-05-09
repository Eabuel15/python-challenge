import os
import csv

csvpath = os.path.join(".", "PyPoll" ,"Resources", "election_data.csv")

#variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)

    for row in csvreader:
        #total votes cast calculator
        total_votes += 1

        #each candidates total votes
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

    khan_percent = (khan_votes/total_votes)
    correy_percent = (correy_votes/total_votes)
    li_percent = (li_votes/total_votes)
    otooley_percent = (otooley_votes/total_votes)

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Khan: {khan_percent: .3%} ({khan_votes})")
print(f"Correy: {correy_percent: .3%} ({correy_votes})")
print(f"Li: {li_percent: .3%} ({li_votes})")
print(f"O'Tooley: {otooley_percent: .3%} ({otooley_votes})")