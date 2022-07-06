# import os module to allow file packing
import os

#import the csv module that will allow for us to handle .csv files
import csv

#create a path to the csv
filePath = os.path.join("Resources", "election_data.csv")

#open the file using the file path above
with open(filePath) as file:
  #use csv.reader() function to open the file
    csvReader =csv.reader(file, delimiter =",")

    #read the header row first
    header = next(csvReader)

    #create an empty array for candidate and votes
    #this array will look contain a list of dictionary
    #there will be one dictionary per candidate
    #so it will look like this in the end
    #[
    # { 'name': 'Charles Casper Stockham', 'votes': 85213},
    # { 'name': 'Diana DeGette', 'votes': 272892},
    # { 'name': 'Raymon Anthony Doane', 'votes': 11606}
    # ]

    candidate_array = []

    #loop through each row in the table
    for row in csvReader:
      candidate_name = row[2]

      #find if the candidate already has an entry in the list of dictionaries
      #here we are searching by name
      #if the candidate is not in the list already, return None
      #we'll use this None to evaluate if we need to create an entry for the candidate
      existing_candidate = next((candidate for candidate in candidate_array if candidate['name'] == candidate_name), None)

      if existing_candidate:
        #if a candidate was found, increate the vote count by 1
        existing_candidate['votes'] = existing_candidate['votes'] + 1
      else:
        #if a candidate was NOT found, create an entry for the candidate and initialize the vote to 1
        candidate_array.append({ 'name': candidate_name, 'votes': 1})
    
    total_votes = 0
    #loop through the candidates in the array and add up each candidates votes into a total (85213 + 272892 + 11606)
    for candidate in candidate_array:
      total_votes = total_votes + candidate['votes']

    print(f"Total votes: {total_votes}")

    votes_winner = 0
    candidate_winner = None

    #loop through each candidate and calculate percentage and find a winner
    for candidate in candidate_array:
      # canculate percentage with 3 decimal places
      percentage = float("{0:.3f}".format(candidate['votes'] / total_votes * 100))
      print(f"{candidate['name']}: {percentage}% ({candidate['votes']})")

      #if the candidate's votes are greater than the previous candidate's votes, 
      # set our new winner and set the new winner vote count to votes_winner
      if candidate['votes'] > votes_winner:
        candidate_winner = candidate['name']
        votes_winner = candidate['votes']

    print(f"Winner: {candidate_winner}")