#tool to be used to import 
import os
import csv

#Created path so csv file can be read
csvpath = os.path.join('/Users/papilex/python-challenge/PyBank/main.py/Resources/budget_data.csv')

#defining variables
total_profit_losses = 0
total_months = 0 
changes = []
greatest_increase = 0
greatest_increase_date = " "
greatest_decrease = 0
greatest_decrease_date = " "

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter= ',')

    #skip header
    next(csvfile)


    #for loop for months count
    for row in csvreader:
        
        #sum of profit losses
        total_profit_losses += int(row[1])

        #sum of total months
        total_months += 1

        #Cal for change in prof/losses + adding it to list "Change" + finding greatest increase/decrease
        if total_months > 1:
            change = int(row[1]) - prev_profit_losses
            changes.append(change)
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            elif change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]
        prev_profit_losses = int(row[1])

#Average change 
if len(changes) > 0:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

#Creating a file to write results
output_file = open("budget_data_solution.txt", "w")

#Writing output on file 
output_file.write("Financial Analysis\n")
output_file.write("------------------------------------\n")    
output_file.write("Total Months: " + str(total_months) + "\n")
output_file.write("Total Profit/Losses: $" + str(total_profit_losses)+ "\n")    
output_file.write("Average Change: $" + str(round(average_change,2)) + "\n")
output_file.write("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")" + "\n")
output_file.write("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")" + "\n")

#Closing writing file 
output_file.close()

print("Financial Analysis")
print("------------------------------------")    
print("Total Months: " + str(total_months))
print("Total Profit/Losses: $" + str(total_profit_losses))    
print("Average Change: $" + str(round(average_change,2)))
print("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")

