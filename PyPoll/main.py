# import libraries

import os
import csv


# add csv path
csvpath = os.path.join("election_data.csv")

# add variables
total = 0
khan = 0
correy = 0
li = 0
otooley = 0


with open(csvpath,newline="") as file:
    csvreader = csv.reader(file,delimiter=",")
    header = next(csvreader)

        
    for row in csvreader:   
        # total votes = total rows 
        total += 1
        
        # add votes to each candidate
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        else: 
            otooley += 1
    
    # calculate percentages
    k_percentage = round(100*(khan / total),1)
    c_percentage = round(100*(correy / total),1)
    l_percentage = round(100*(li / total),1)
    o_percentage = round(100*(otooley / total),1)
    
    
    #find winner
    votes_dict = {"Khan":khan,"Correy":correy,"Li":li,"O'Tooley":otooley}
    winner_votes = max([khan,correy,li,otooley])
    for key,value in votes_dict.items(): 
        if value == winner_votes:
            winner = key
            

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total))
print("-------------------------")
print("Khan: " + str(k_percentage) + "% (" + str(khan) + ")")
print("Correy: " + str(c_percentage) + "% (" + str(li) + ")")
print("Li: " + str(l_percentage) + "% (" + str(li) + ")")
print("O'Tooley: " + str(o_percentage) + "% (" + str(otooley) + ")")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")


# export data to txt file

with open("Election_Results.txt", "w") as text_file:
    text_file.write("Election Results")
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")
    text_file.write("Total Votes: " + str(total))
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")
    text_file.write("Khan: " + str(k_percentage) + "% (" + str(khan) + ")")
    text_file.write("\n")
    text_file.write("Correy: " + str(c_percentage) + "% (" + str(li) + ")")
    text_file.write("\n")
    text_file.write("Li: " + str(l_percentage) + "% (" + str(li) + ")")
    text_file.write("\n")
    text_file.write("O'Tooley: " + str(o_percentage) + "% (" + str(otooley) + ")")
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")
    text_file.write("Winner: " + str(winner))
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.close()