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

print(total_votes)
print(khan_votes)
print(correy_votes)
print(li_votes)
print(otooley_votes)