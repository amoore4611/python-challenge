# import os module to allow file packing
import os

#import the csv module that will allow for us to handle .csv files
import csv

#create a path to the csv
filePath = os.path.join("Resources", "budget_data.csv")

#create an output file to put results to text
outputFile = os.path.join("Analysis", "FinancialAnalysis.txt")

#variables
total_months = 0 #variable to hold the months
total_Profits = 0 #variable to hold net profit/loss
average_change = [] #empty list for average change in profit/loss
months = [] #empty list for months

#open the file using the file path above
with open(filePath) as file:

    #use csv.reader() function to open the file
    csvReader =csv.reader(file, delimiter =",")

    #read the header row first
    header = next(csvReader)

    #move to the first row
    firstRow = next(csvReader)

    #establish the previous profit/loss
    #profit/loss is in index 1
    previous_profit_loss = float(firstRow[1])

    #increment the count of the total months
    total_months += 1 #same as the total_months = total_months + 1
        
    #add onto the total amount of revenue by converting string to number
    total_Profits += float(firstRow[1])

    #read the rows in the CSV file
    for row in csvReader:
        #increment the count of the total months
        total_months += 1 #same as the total_months = total_months + 1
        
        #add onto the total amount of revenue by converting string to number
        total_Profits += float(row[1])

        #calculate the net change of the profit/loss
        netChange = float(row[1]) - previous_profit_loss

        #add on to the list of average_change
        average_change.append(netChange)

        #add first month a change occured in profit/loss
        #month is in index 0
        months.append(row[0])

        #update the previous profit/loss
        previous_profit_loss = float(row[1])

#calcualte the average net change 
average_change_profit_loss = sum(average_change) / len(average_change)

greatestIncrease = [months[0], average_change[0]] #holds the month and the value of the greatest increase
greatestDecrease = [months[0], average_change[0]] #holds the month and the value of the greatest decrease

#use loop to calculate the index of the greatest and least average change
for change in range(len(average_change)):
    #calculate the greatest increase and decrease
    if(average_change[change] > greatestIncrease[1]):
        #if the value is greater than the greatest increase, that value becomes the new greatest increase
        greatestIncrease[1] = int(average_change[change])
        # udpate the month
        greatestIncrease[0] = months[change]
    
    if(average_change[change] < greatestDecrease[1]):
        #if the value is less than the greatest decrease, that value becomes the new greatest decrease
        greatestDecrease[1] = int(average_change[change])
        # udpate the month
        greatestDecrease[0] = months[change]    

 #create an output variable to hold the output
output = (
  f"\n\nFinancial Analysis\n"
  f"----------------------\n"
  f"Total Months: {total_months}\n" 
  f"Total: ${int(total_Profits):,}\n"
  f"Average Change: ${float(average_change_profit_loss):,.2f}\n"
  f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n"
  f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n" 
)
#displays the output to the console/terminal
print(output)

  #print the results and export the data to a text file
with open(outputFile, 'w') as textFile:
  #write the output to the text file
  textFile.write(output)
