# Election_Analysis

## Project Overview
Employees from the Colorado Board of Elections need to go over the recent election results to determine how many votes each candidate recieved, the perentage of votes recieved by each candidate, the number of total votes casted, and the winner of the election based on the popular vote.


## Election-Audit Results 

### How many votes were cast in this congressional election?

Total votes was found by setting the vote count variable to 0 then for loops were used to add an additional vote to the counter.

![total votes](https://github.com/vanessaneang/Election_Analysis/blob/main/Resources/total_votes.png)

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

### Which county had the largest number of votes?

  - **Denver** had the largest number of votes with **306,055 votes**.
  - **Jefferson** was the second largest number of votes with **38,855 votes**.
  - **Arapahoe** had the smalles number of votes with **24,801 votes**.

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
![percentage_total_by_candidate](https://github.com/vanessaneang/Election_Analysis/blob/main/Resources/total_votes.png)

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

![winner](https://github.com/vanessaneang/Election_Analysis/blob/main/Resources/total_votes.png)

## Election-Audit Summary
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
