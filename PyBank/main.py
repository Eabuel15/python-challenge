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
csvpath = os.path.join("..", "PyBank" ,"Resources", "budget_data.csv")

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

    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_amt}")
    print(f"Average Change: ${avg_changes}")
    print(f"Greatest Increase in Profits: {profit_inc_month} (${profit_inc})")
    print(f"Greatest Decrease in Profits: {loss_dec_month} (${loss_dec})")

    output_file = os.path.join("..", "PyBank", "analysis", "PyBank_output.txt")
    with open(output_file,"w") as txtfile:

        txtfile.write(f"Financial Analysis")
        txtfile.write(f"\n----------------------------")
        txtfile.write(f"\nTotal Months: {total_months}")
        txtfile.write(f"\nTotal: ${net_amt}")
        txtfile.write(f"\nAverage Change: ${avg_changes}")
        txtfile.write(f"\nGreatest Increase in Profits: {profit_inc_month}(${profit_inc})")
        txtfile.write(f"\nGreatest Decrease in Profits: {loss_dec_month}(${loss_dec})")