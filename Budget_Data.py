# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

mypath = 'C:/Users/dbik/Documents/GitHub/Resources'

budgetCSV = os.path.join(mypath, 'budget_data.csv')

# Improved Reading using CSV module
with open(budgetCSV, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    header = next(csvreader)

    # Initialize variables
    rows = 0
    total = 0
    Profit = 0
    Loss = 0
    row_profit = 0
    row_loss = 0
    Max = 0
    Min = 0

# Loop through the data

for row in csvreader:
    rows += 1

    total = total + int(row[1])

    if (int(row[1]) > 0):
        Profit = Profit + int(row[1])
        row_profit += 1
    else:
        Loss = Loss + int(row[1])
        row_loss += 1

    # Find Greatest increase and decrease in profits (date and amount) over the entire period

    if (int(row[1]) > Max):
        Max = int(row[1])
        Month_max = row[0]
    elif (int(row[1]) < Min):
        Min = int(row[1])
        Month_min = row[0]

Average_Change = ((Profit / row_profit) + (Loss / row_loss)) / 2

# Print the analysis

print("Financial Analysis")
print("-----------------------\n")
print(f"Total Months: {str(rows)} \n")
print(f"Total: ${str(total)}\n")
print(f"Average Change: ${str('%.2f' % Average_Change)}\n")
print(f"Greatest Increase in Profits: {Month_max} (${str(Max)})\n")
print(f"Greatest Decrease in Profits: {Month_min} (${str(Min)})\n")

# Export a text file with the results

# Save the output file path
results_file = os.path.join("results.csv")