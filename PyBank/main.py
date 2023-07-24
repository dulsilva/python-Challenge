import csv
import os

# Set the path for the csv file
budget_data_csv = "Resources/budget_data.csv"

# Initialize the variables to hold data
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the csv file
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through the rows in the csv file
    for row in csvreader:

        # Count the total number of months in the dataset
        total_months += 1

        # Calculate the total profit/loss over the entire period
        total_profit_loss += int(row[1])

        # Calculate the change in profit/loss between the current row and the previous row
        profit_loss_change = int(row[1]) - prev_profit_loss
        prev_profit_loss = int(row[1])

        # Find the greatest increase in profits (date and amount) over the entire period
        if (profit_loss_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

        # Find the greatest decrease in losses (date and amount) over the entire period
        if (profit_loss_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# Calculate the average change in profit/loss over the entire period
average_change = round(total_profit_loss/total_months, 2)

# Print the financial analysis to the console
Output_txt= os.path.join('analysis','output.txt')
with open (Output_txt,'w') as file:
        file.write("Financial Analysis" + "\n")
        file.write("----------------------------" + "\n")
        file.write(f"Total Months: {total_months}" + "\n")
        file.write(f"Total: ${total_profit_loss}" + "\n")
        file.write(f"Average Change: ${average_change}" + "\n")
        file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})" + "\n")
        file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})" + "\n")

