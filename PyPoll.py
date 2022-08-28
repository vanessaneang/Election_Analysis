# The data we need to retrieve.
# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

# import datetime
# now = datetime.datetime.now()
# print("The time right now is", now)

import random
import csv

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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    # print(election_data)
    # To do: read and analyze data here.
    # Read the file object with the reader function.    
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    # for row in file_reader:
        # print(row)





# using the open fcn w/ the "w" mode we will write data to the file
#use the open statement to open the file as a text file.
# with open(file_to_save, "w") as txt_file:
# # write some data to the file.
#     # write three counties to the file.
#     txt_file.write("Counties in the Elections\n------------------------\nArapahoe\nDenver\nJefferson")



    
