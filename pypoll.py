#Add dependencies
import csv
import os

#Add variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# dd a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a total vote counter
total_votes = 0

#Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

#Create a county list and county votes dictionary
county_list = []
county_votes = {}

#Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track the largest county and county voter turnout
largest_county = ""
Largest_county_turnout = 0
Largest_county_percentage = 0
county_voter_turnout = 0
county_percentage = 0

#Read csv and convert it into list of dict
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    #Read the header
    header = next(reader)
    #For each row in the CSV file
    for row in reader:

        #Add to the total vote count
        total_votes = total_votes + 1
        #Get the candidate name from each row
        candidate_name = row[2]
        #Extract the county name from each row
        county_name = row[1]

        #If candidate does not match existing candidate add it to list
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #Write if statement that checks that county does not match existing county in the list
        if county_name not in county_list:

            #Add the existing county to the list of counties
            county_list.append(county_name)

            #Begin tracking the county's vote count
            county_votes[county_name] = 0

        #Add a vote to that county's vote count.
        county_votes[county_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    #Write a for loop to get the county from the county dictionary.
    for county_name in county_list:

        #Retrieve county vote count
        county_voter_turnout = county_votes[county_name]

        #Calculate percentage of votes for the county
        county_percentage = float(county_voter_turnout) / float(total_votes) * 100

        #Print the county results to the terminal
        county_results = (f"{county_name}: {county_percentage:.1f}% ({county_voter_turnout:,})\n")
        print(county_results)

        #Save the county votes to a text file
        txt_file.write(county_results)

        #Write an if statement to determine the winning county and get its vote count
        if (county_voter_turnout > Largest_county_turnout) and (county_percentage > Largest_county_percentage):
            Largest_county_turnout = county_voter_turnout
            largest_county = county_name
            Largest_county_percentage = county_percentage

    #Print county with the largest turnout to the terminal
    county_results2 = (
        f"\n-------------------------\n"
        f"Largest County Turnout is {largest_county}\n"
        f"-------------------------\n")

    print(county_results2)

    #Save the county with the largest turnout to a text file
    txt_file.write(county_results2)

    #Save the final candidate vote count to the text file
    for candidate_name in candidate_votes:

        #Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Print candidates voter count and percentage to terminal
        print(candidate_results)
        #Save the candidate results to text file
        txt_file.write(candidate_results)

        #Determine winning vote count, percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #Print the winning candidate to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #Save the winning candidate's name to text file
    txt_file.write(winning_candidate_summary)