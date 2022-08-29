
import csv
import os

# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a file name variable to a dricect or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Create county list, empty dictionary, county tracter, and Count county votes
county_list = []
total_county_votes = {}
largest_county_vote = ""
largest_vote = 0
largest_vote_percentage = 0


# Create candidates option list
candidate_options = [] 

# Create empty dictionary to link candidates with their votes
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
        
        #Print county names from each row
        county_names = row[1]


        

        





        # # If county does not match any existing counties
        if county_names not in county_list:

            county_list.append(county_names)
        
            total_county_votes[county_names] = 0
        
        total_county_votes[county_names] += 1

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
            f"---------------------------\n"
            f'County Votes:\n')
        
        print(election_data, end="")

        #Save the final vote count to the text file.
        txt_file.write(election_results)
        
        for county_names in total_county_votes:

            # 2. Retrieve vote count of candidate
            county_votes = total_county_votes[county_names]

            # 3. Calculate the percentage of votes.
            county_vote_percentage = float(county_votes)/float(total_votes) * 100

            county_results = (f"{county_names}: {county_vote_percentage:.1f}% ({county_votes:,})\n"
            )
            #To-do save to txt.file
            print(county_results)
            txt_file.write(county_results)         

            #Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.

            if (county_votes > largest_vote) and (county_vote_percentage > largest_vote_percentage):

                # 2. If true set winning_count = votes and winning percent= vote percent
                largest_vote = county_votes
                largest_vote_percentage = county_vote_percentage

                # 3. Set the winning_candidate equal to the candidate's name
                largest_county_vote = county_names
        largest_county_summary = (
            f"------------------------\n"
            f"Largest County Turnout: {largest_county_vote}\n"
            f"------------------------\n"
        )
        print(largest_county_summary)
        txt_file.write(largest_county_summary) 
    # Get candidate's vote total percentage.
        #1. iterate through the candidate list.

        for candidate_name in candidates_votes:

            # 2. Retrieve vote count of candidate
            votes = candidates_votes[candidate_name]

            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            # 4. Print the candidate name and percentage of votes.
            candidate_results = (
                f"{candidate_name}: recieved {vote_percentage:.1f}% ({votes:,})\n"
                )
            # print each candidate their voter count, and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.
            txt_file.write(candidate_results)
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
            




