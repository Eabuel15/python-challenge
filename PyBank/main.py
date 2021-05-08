import os
import csv

#variables
total_months = 0
net_amt = 0
profit_inc = 0
profit_inc_month = 0
loss_dec = 0
loss_dec_month = 0

month_count = []
monthly_change = []

#"." for VS Code, ".." for Terminal Gitbash
csvpath = os.path.join(".", "PyBank" ,"Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    row = next(csvreader)

    previous_profit = int(row[1])
    total_months += 1
    net_amt += int(row[1])
    profit_inc = int(row[1])
    profit_inc_month = row[0]

    for row in csvreader:
        total_months += 1
        net_amt += int(row[1])

        #calculate change from current month to prev month
        change = int(row[1]) - previous_profit
        monthly_change.append(change)
        previous_profit = int(row[1])
        month_count.append(row[0])

        #calculate profit increase
        if int(row[1]) > profit_inc:
            profit_inc = int(row[1])
            profit_inc_month = row[0]
        #calculate loss decrease        
        if int(row[1]) < loss_dec:
            loss_dec = int(row[1])
            loss_dec_month = row[0]
        
    avg_changes = sum(monthly_change)/len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(net_amt))
    print("Average Change: $" + str(avg_changes))
    print("Greatest Increase in Profits: " + profit_inc_month + "($" + str(profit_inc) + ")")
    print("Greatest Decrease in Profits: " + loss_dec_month + "($" +str(loss_dec) + ")")

    PyBank = open("output.txt","w+")
    PyBank.write("Financial Analysis")
    PyBank.write("\n" + "----------------------------")
    PyBank.write("\n" + "Total Months: " + str(total_months))
    PyBank.write("\n" + "Total: $" + str(net_amt))
    PyBank.write("\n" + "Average Change: $" + str(avg_changes))
    PyBank.write("\n" + "Greatest Increase in Profits: " + profit_inc_month + "($" + str(profit_inc) + ")")
    PyBank.write("\n" + "Greatest Decrease in Profits: " + loss_dec_month + "($" +str(loss_dec) + ")")