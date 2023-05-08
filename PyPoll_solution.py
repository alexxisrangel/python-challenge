#Tools needed to import
import os
import csv

#path in order to read csv file 
csvpath = os.path.join('/Users/papilex/python-challenge/PyPoll/Resources/election_data.csv')

#defining variables 

candidates = {}

#Opening csvfile to create loop
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    
    
    #skipping header
    next(csvfile)

    #for loop for calcualtions 
    for row in csvreader:

        #selecting column with list of candidates
        candidate = (row[2])

        if candidate not in candidates:
            candidates[candidate] = 0
            
        candidates[candidate] += 1

total_votes = sum(candidates.values())

#creating path for outputfile 
output_file = open("election_data_solution.txt", "w")


print("Election Results " )
output_file.write("Election Results \n")
print("------------------------")
output_file.write("------------------------\n")
print(f"Total Votes:{total_votes}")
output_file.write(f"Total Votes:{total_votes}\n")
print("------------------------")
output_file.write("------------------------\n")


for candidate in candidates:
    #calculating vote percentage for each candidate 
    vote_percentage = candidates[candidate] / total_votes * 100


    print(f"{candidate}: {vote_percentage: .3f}% ({candidates[candidate]})")
    output_file.write(f"{candidate}: {vote_percentage: .3f}% ({candidates[candidate]})\n")

#I searched the web for .get, used this resource : https://www.scaler.com/topics/get-in-python/
winner = max(candidates, key = candidates.get)


print("------------------------")
output_file.write("------------------------\n")
print(f"Winner: {winner}")
output_file.write(f"Winner: {winner}\n")
print("------------------------")
output_file.write("------------------------\n")

