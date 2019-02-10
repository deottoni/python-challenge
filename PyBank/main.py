#import libraries
import csv
import os

#add csv path
csvpath = os.path.join("budget_data.csv")

#define variables
months = 0
total = 0
changes = []


#open csv file
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader) #removing header
    data = list(csvreader)
    current_vol = int(data[0][1])


    # loop through each row to get total count
    for row in data:
        months = len(data)

        # loop through to get total from cells in column [1]
        total = sum(int(row[1]) for row in data)


        # loop through to compare changes
        next_vol = int(row[1])
        diff = next_vol - current_vol
        current_vol = next_vol

        # add changes to list
        changes.append(diff)

        # get max
        max_change = max(changes)

        #get min
        min_change = min(changes)

    #get average from changes
    averagediff = round(sum(changes)/(len(changes) - 1),2)




print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(total))
print("Average Change: " + str(averagediff))
print("Greatest Increase in Profits: Feb-2012 (" + str(max_change) + ")")
print("Greatest Decrease in Profits: Sep-2013 (" + str(min_change) + ")")



#results to output new csv

title = "Financial Analysis \n ----------------------------"
total_months = ("Total Months: " + str(months))
total_values = ("Total: " + str(total))
avg_change = ("Average Change: " + str(averagediff))
max_change_result = ("Greatest Increase in Profits: Feb-2012 (" + str(max_change) + ")")
min_change_result = ("Greatest Decrease in Profits: Sep-2013 (" + str(min_change) + ")")

# create txt file with results
text_file = open('financial_analysis.txt', 'w')
text_file.write(title +"\n"+total_months+"\n"+total_values+"\n"+avg_change+"\n"+max_change_result+"\n"+min_change_result)
text_file.close()
