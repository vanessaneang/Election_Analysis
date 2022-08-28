#print("Hello World!")
#help("keywords")
# first = 5 + 2 * 3
# print(first)
# second = 8 // 5 - 3
# print(second)
# third = 8 + 22 * 2 - 4
# print(third)
# fourth = 16 - 3 / 2 + 7 - 1
# print(fourth)
# fifth = 3 ** 3 % 5
# print(fifth)
# sixth = 5 + 9 * 3 / 2 - 4
# print(sixth)
# firstp = (5 + 2) * 3
# secondp =(8 // 5) - 3
# thirdp = 8 + (22 * (2 - 4))
# fourthp = 16 - 3 / (2 + 7) - 1
# fifthp =3 ** (3 % 5)
# sixthp = 5 + (9 * 3 / 2 - 4) 
# seventhp= 5 + (9 * 3 / (2 - 4))

# print(firstp)
# print(secondp)
# print(thirdp)
# print(fourthp)
# print(fifthp)
# print(sixthp)
# print(seventhp)

# counties = ["Arapahoe","Denver","Jefferson"]
# print(counties)
# counties.append("El Paso")
# print(counties)
# counties.insert(2,"El Paso")
# print(counties)
# counties.remove("El Paso")
# print(counties)
# counties.pop(3)
# print(counties)
# counties.insert(1, "El Paso")
# counties.pop(0)
# print(counties)
# counties.insert(1,"Jefferson")
# counties.pop(3)
# print(counties)
# counties.append("Araphaoe")
# print(counties)

# x = 10
# y = 20
# if x <10:
#     if y >20:
#         print("y is greater than 20 when x is less than 10")
#     else:
#         print("y is less than 20 when x is less than 10")
# else:
#     print("x is greater than 10")
    
# Create an empty dictionary with dictionary_name = {}
# counties_dict ={}

# counties_dict["Arapahoe"] = 422829

# # print(counties_dict)

# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438

# # print(counties_dict)

# print(len(counties_dict))

# print(counties_dict.items())


# # make a list of dictionaries where county and registered voters are keys
# voting_data = []

# # can treat list of dictionaries with same rules as lists

# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# print(voting_data)

# print(len(voting_data))

# voting_data.insert(2, {"county": "El Paso", "resgistered_voters": 461149})
# voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.remove({"county":"Denver", "registered_voters": 463353})

# print(voting_data)

# voting_data.insert(2, ({"county":"Denver", "registered_voters": 463353}))
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# print(voting_data)

# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# if statements for python
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

#if-else statements
# temperature = int(input("What is the temperature outside?"))
# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# nested if-else statements

# score = int(input("What is your test score?"))

# if score >=90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')

# these nested if-else can also be if-elif-else statements

# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D')
# else:
#     print('Your grade is an F.')



# counties = ["Arapahoe","Denver","Jefferson"]
# if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# while loops until statement is false be careful because it'll go into an infinite loop if not correctly defined/stopped
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

#for loops use for xxxx in xxxx

# counties = ["Arapahoe","Denver","Jefferson"]
# for county in counties:
#     print(county)

# for loop with range function

# numbers = [ 0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

from itertools import count


# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict.keys():
#     print(county)
# for county in counties_dict:
#     print(counties_dict.get(county))
# for county in counties_dict:
#     print(county)
# for county, voters in counties_dict.items():
#     print(county, voters) 
# for county, voters in counties_dict.items():
#     print('{} county has {} number of voters.'.format(county, voters))
#     print(f"{county} county has {voters} registered voters.")

#using range fuction with list of dictionaries in a for loop

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in range(len(voting_data)):
#     print(voting_data[county_dict]['county'])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

#Using f strings for values
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
# print(f"I recieved {my_votes / total_votes*100}% of the total votes.")

#practice for f strings

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f"{county} has {voters} registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# for county in range(len(voting_data)):
#     print(f"{voting_data[county]['county']} has {voting_data[county]['registered_voters']} registered voters.")


import os
import shutil

shutil.move("../neang/Election_Analysis/election_results.csv", "../neang/Election_Analysis/Resources/election_results.csv")