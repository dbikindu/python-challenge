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

    # Initialize variables to calculate the average change between months
    PL_change = 0
    Total_PL_list = []
    Month_change = 0
    PL_change_list = []
    Total_months_list = []
    current_PL = 0
    last_PL = 0

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

        # Find the average in "Profit/Losses" between months over the entire period

        Total_months_list.append(row[0])
        Total_PL_list.append(int(row[1]))

            # Find Greatest increase and decrease in profits (date and amount) over the entire period

        if (int(row[1]) > Max):
            Max = int(row[1])
            Month_max = row[0]
        elif (int(row[1]) < Min):
            Min = int(row[1])
            Month_min = row[0]

    for i in range(len(Total_PL_list) - 1):
        PL_change_list.append(Total_PL_list[i + 1] - Total_PL_list[i])

    Average_change = (sum(PL_change_list)) / (len(PL_change_list))


# Print the analysis
print("Financial Analysis")
print("-----------------------\n")
print(f"Total Months: {str(rows)} \n")
print(f"Total: ${str(total)}\n")
print(f"Average Change: ${str('%.2f' % Average_change)}\n")
print(f"Greatest Increase in Profits: {Month_max} (${str(Max)})\n")
print(f"Greatest Decrease in Profits: {Month_min} (${str(Min)})\n")

# Export a text file with the results
results_file = ('C:/Users/dbik/Documents/GitHub/python-challenge/Summary.txt')

# Save the output file path
with open(results_file, 'w') as file:
    file.write("Financial Analysis")
    file.write("-----------------------\n")
    file.write(f"Total Months: {str(rows)} \n")
    file.write(f"Total: ${str(total)}\n")
    file.write(f"Average Change: ${str('%.2f' % Average_change)}\n")
    file.write(f"Greatest Increase in Profits: {Month_max} (${str(Max)})\n")
    file.write(f"Greatest Decrease in Profits: {Month_min} (${str(Min)})\n")