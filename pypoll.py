import _csv
import os

#Assign variable for file to load
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results
election_data = open(file_to_load, 'r')
with open(file_to_load, 'r') as election_data:

#Create filename variable to a direct or indirect path to file
    file_to_save = os.path.join("anaylsis", "election_analysis.txt")

#To do,  perform analysis
#Use the reader function
file_reader = open(file_to_load, 'r')
#Print rows in the csv file
for row in file_reader:
    print(row)

#Read and print header row
headers = next(file_to_load, 'r')
    print(headers)

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