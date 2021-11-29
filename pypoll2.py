#Add dependencies
import csv
import os

#Assign variable for file to load
file_to_load = os.path.join("Resources", "election_results.csv")
#Create filename variable to a direct or indirect path to file
file_to_save = os.path.join("anaylsis", "election_analysis.txt")

#Initialize total vote count
total_votes = 0
#Candidate options
candidate_options = []
#Declare empty dictionary
candidate_votes = {}
#Winning candidate and winning count
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results
election_data = open(file_to_load, 'r')
with open(file_to_load, 'r') as election_data:

#To do,  perform analysis
#Use the reader function
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

#Print rows in the csv file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1    

        #Print candidate name from each row
        candidate_name = row[2]

#If candidate does not match an existing.
        if candidate_name not in candidate_options:
            #Add to list of candidates
            candidate_options.append(candidate_name)
            #Track candidate vote count
            candidate_votes[candidate_name] = 0
        #Add vote to candidates count
        candidate_votes[candidate_name] += 1


#Determine percentage of votes for each candidate
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) *100, 1

#Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")


#Print the candidate list
print(candidate_options)
#Print total votes
print(total_votes)
#Print candidate vote dict
print(candidate_votes)
#Print candidate name and percentage of votes
print(f"{candidate_name}: received {vote_percentage}% of the vote.")
#Print candidate name, vote count, percentage of votes
print(f"{candidate_name}: {vote_percentage:.1f%}: ({votes:,})\n")
#Print winning candidate summary
print(winning_candidate_summary)



#Use open funciton with "w" mode to write data to file
open(file_to_save, "w")
#Use open statement to open the created text file
outfile = open(file_to_save, "w")
#Write data to election_analysis.exe
outfile.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")
#Close created file
outfile.close()


#Close file
election_data.close()