# Election_Analysis

## Project Overview
Employees from the Colorado Board of Elections need to go over the recent election results to determine how many votes each candidate recieved, the perentage of votes recieved by each candidate, the number of total votes casted, and the winner of the election based on the popular vote.


## Election-Audit Results 

### How many votes were cast in this congressional election?

Total votes was found by setting the vote count variable to 0 then for loops were used to add an additional vote to the counter.

![total votes](https://github.com/vanessaneang/Election_Analysis/blob/main/Resources/total_votes.png)

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

In order to find the breakdown of voters for each county we needed to create the variables to hold specific values, such as lists, and dictionaries. The hardest part of this code was making sure the for loops correlated to the correct outputs.

```Ruby
# Create county list, empty dictionary, county tracter, and Count county votes
county_list = []
total_county_votes = {}
largest_county_vote = ""
largest_vote = 0
largest_vote_percentage = 0
```
```Ruby
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
```        

### Which county had the largest number of votes?

  - **Denver** had the **largest** number of votes with **306,055 votes**.
  - **Jefferson** was the second largest number of votes with **38,855 votes**.
  - **Arapahoe** had the smalles number of votes with **24,801 votes**.
  - 
![total votes](https://github.com/vanessaneang/Election_Analysis/blob/main/Resources/county_turnout.png)


### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

By using a list for the candidates options, which was created before the "with open" file command along with a candidates votes dictionary we were able to link the candidate names to the number of votes they recieved.

```ruby
# Create candidates option list
candidate_options = [] 

# Create empty dictionary to link cadidates with their votes
candidates_votes = {}
```
 These were iterated within the for loop with a nested if function to append the list of candidates. 
 
```ruby
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Create key from unique candidates. Begin tracking candidate;s votes.
            candidates_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidates_votes[candidate_name] += 1
```

Then in order to get the vote total percentage we needed to creat another for loop within the for loop to iterate through the candidates list.  

```ruby
 #1. iterate through the candidate list.
        for candidate_name in candidates_votes:

            # 2. Retrieve vote count of candidate
            votes = candidates_votes[candidate_name]

            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            # 4. Print the candidate name and percentage of votes.
            candidate_results = (f"{candidate_name}: recieved {vote_percentage:.1f}% ({votes:,})\n")
            # print each candidate their voter count, and percentage to the terminal.
            print(candidate_results)
```
![percentage_total_by_candidate](https://github.com/vanessaneang/Election_Analysis/blob/main/Resources/percentage_of_votes_by_candidates.png)

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

To determine the winning candidate several variables needed to be defined and set to the right parameters before the "with open" function, winning_candidate as a string, winning_count as 0, and winning_percentage as 0.
```ruby
# create winning_count tracker and candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0
```
Then within the for loop for the candidate options we needed to create a nested if condition to iterate the through the loop to determine the winning candidate name and percentage.

```ruby
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
```
![winner](https://github.com/vanessaneang/Election_Analysis/blob/main/Resources/winning_candidate.png)

## Election-Audit Summary

This script can be used for other elections in a few ways: (1) by continuously updating the path for the csv file to use the most current file the most current election can be tracked and (2) change the output file to place the results into an excel file or csv instead so further analysis over trends throughout the years could be tracked to compare if there are specific candidate parties the constituents may choose, which can serve as a predictive election anlaysis model for the future. 

