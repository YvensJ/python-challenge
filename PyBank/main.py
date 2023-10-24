import os
import csv

#variables used
count = 0
value = 0
total_value = 0
pre_value = 0
change_time = 0 
change = []
avg = 0.00
inc = 0
dec= 0

#create path to csv file
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

#open and read csv file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

 #keep header code to make sure header row is not counted for total months 
    csv_header = next(csv_file)
    
    for row in csv_reader:

        #give count for months
        count += 1

        #the net total amount of "Profit/Losses"
        value = int(row[1])
        total_value = (total_value + value)

        #the change over time
        change_time = (value - pre_value) 
        change.append(change_time)
        pre_value = int(row[1])

        #greatest increase
        if change_time > inc:
            inc = change_time 
            inc_month = row[0]
        #greatest decrease
        if change_time < dec:
            dec = change_time
            dec_month = row[0]

change.pop(0)

#function used to find change over time 
def average(numbers):
    length =len(numbers)
    total = 0.0
    for number in numbers:
        total += number 
    return total/length 
avg = average(change)    
avg = round(avg, 2)

#print results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total_value}")
print(f"Average Change: ${avg}")
print(f"Greatest Increase in Profits: {inc_month} (${inc})")
print(f"Greatest Decrease in Profits: {dec_month} (${dec})")

#create lines to wrtie results in text file
lines = [(f"Financial Analysis"), (f"Total Months: {count}"), (f"Total: ${total_value}"), 
         (f"Average Change: ${avg}"), (f"Greatest Increase in Profits: {inc_month} (${inc})"), 
         (f"Greatest Decrease in Profits: {dec_month} (${dec})")]


path = os.path.join(".", "analysis", "Analysis.txt")
with open(path, 'w') as a:

    for line in lines:
        a.write(line)
        a.write('\n')