# The data we need to retrieve.
# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

# import datetime
# now = datetime.datetime.now()
# print("The time right now is", now)

# import random
# import csv

# from datetime import datetime
# # print(dir(csv))
# print(dir(int))
# print(dir(float))
# print(dir(list))
# print(dir(tuple))
# print(dir(dict))
# print(dir(datetime))

import csv
import os

# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a file name variable to a dricect or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Create candidates option list
candidate_options = [] 

# Create empty dictionary to link cadidates with their votes
candidates_votes = {}

# create winning_count tracker and candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    # print(election_data)
    # To do: read and analyze data here.
    # Read the file object with the reader function.    
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
 
    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]
        
        # If the candidate does not match any exiting candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Create key from unique candidates. Begin tracking candidate;s votes.
            candidates_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidates_votes[candidate_name] += 1

    #Save results to our text file.
    with open(file_to_save, "w") as txt_file:

        election_results = (
            f"\nElection Results\n"
            f"---------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------\n")
        
        print(election_data, end="")

        #Save the final vote count to the text file.
        txt_file.write(election_results)

    # Get candidate's vote total percentage.
        #1. iterate through the caiddate list.

        for candidate_name in candidates_votes:

            # 2. Retrieve vote count of candidate
            votes = candidates_votes[candidate_name]

            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            # 4. Print the candidate name and percentage of votes.
            candidate_results = (f"{candidate_name}: recieved {vote_percentage:.1f}% ({votes:,})\n")
            # print each candidate their voter count, and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.
            txt_file.write(candidate_results)

            #Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.

            if (votes > winning_count) and (vote_percentage > winning_percentage):

                # 2. If true set winning_count = votes and winning percent= vote percent
                winning_count = votes
                winning_percentage = vote_percentage

                # 3. Set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name 
        winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentag: {winning_percentage:.1f}%\n"
            f"------------------------\n"
        )
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
        

