import os
import csv 

total_votes = 0
cand_list = []
cand_vote = []
percents = []
most = 0
win_cand = 0

poll_csv = os.path.join(".", "Resources", "election_data.csv")

with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #skip header row
    csv_header = next(csv_file, None)

    #looping code
    for row in csv_reader:

        #total amount of voters and candidates
        total_votes += 1
        if row[2] not in cand_list:
            cand_list.append(row[2])

    for name in cand_list:
        cand_vote.append(0) 

#loop to get vote amount for each candidate
with open(poll_csv) as csv_file:
    csv_readers = csv.reader(csv_file, delimiter=",")
    next(csv_file, None)

    for row in csv_readers:

        for name in cand_list:           
            v = cand_list.index(name)
            if row[2] == cand_list[v]:
                cand_vote[v] += 1

#loop to get percentage of each vote
for votes in cand_vote:
    vo = cand_vote.index(votes)
    pv = (cand_vote[vo]/total_votes)*100
    pv = round(pv, 3)
    percents.append(pv) 

#find winner
for percent in percents:
    if percent > most:
        win_cand = percents.index(percent)
        most = percent
winner = cand_list[win_cand]

#print results
print(f"Election Results")
print(f"---------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------")

#create lines to wrtie results in text file
lines = [("Election Results"), ("--------------"), (f"Total Votes: {total_votes}"), 
         ("--------------")]

#results for terminal and text file
for name in cand_list:
    e = cand_list.index(name)
    print(f"{cand_list[e]}: {percents[e]}% ({cand_vote[e]})")
    lines.append((f"{cand_list[e]}: {percents[e]}% ({cand_vote[e]})"))

#print results
print(f"---------------------")
print(f"Winner: {winner}")   
print(f"---------------------")

#create lines to wrtie results in text file
lines.append("--------------")
lines.append(f"Winner: {winner}")
lines.append("--------------")

path = os.path.join(".", "analysis", "Analysis.txt")
with open(path, 'w') as text:

    for line in lines:
        text.write(line)
        text.write('\n')