# import os module to allow file packing
import os

#import the csv module that will allow for us to handle .csv files
import csv

#create a path to the csv
filePath = os.path.join("Resources", "election_data.csv")

#create an output file to put results to text
outputFile = os.path.join("Analysis", "ElectionResults.txt")

#open the file using the file path above
with open(filePath) as file:
  #use csv.reader() function to open the file
    csvReader =csv.reader(file, delimiter =",")

    #read the header row first
    header = next(csvReader)

    total_votes = 0 #create a variable hold total votes
    candidate_vote_array = [] #create an empty list to hold candidates
    candidate_vote = {} #dictionary that will hold the votes for each candidate
    winning_count = 0 #variable to hold winning count
    winner = "" #variable to hold winning candidate

    #read the rows in the CSV file
    for row in csvReader:
      total_votes += 1 # same as total_votes = total_votes +1

      #check if candidate is in the list
      if row[2] not in candidate_vote_array:
        #add it to the list of candidates
        candidate_vote_array.append(row[2]) 

        #add the value to the dictionary as well
        #{"key": value}
        #start the count at 1 for the candidates
        candidate_vote[row[2]] = 1
      else:
        # the candidate is in the list of candidates
        #add a vote to that candidate
        candidate_vote[row[2]] += 1
#print(candidate_vote)

vote_output = ""

for candidate in candidate_vote:
  #get the vote count and the percentage of the votes
    vote = candidate_vote.get(candidate)
    vote_per = (float(vote)/ float(total_votes)) * 100.00

    vote_output += f"\t{candidate}: {vote_per:.3f}% ({vote})\n"

    #compare the votes to the winning count
    if vote > winning_count:
      #update the votes to be the new winning count
      winning_count = vote
      #update the winning candidate
      winner = candidate 

winner_output = f"Winner: {winner}\n"

    #create an output variable to hold the output
output = (
  f"\n\nElection Results\n"
  f"----------------------\n"
  f"\tTotal Votes: {total_votes:,}\n" 
  f"----------------------\n"
  f"{vote_output}\n"
  f"----------------------\n"
  f"{winner_output}\n"
  f"----------------------\n"

)
#displays the output to the console/terminal
print(output)

  #print the results and export the data to a text file
with open(outputFile, 'w') as textFile:
  #write the output to the text file
  textFile.write(output)
