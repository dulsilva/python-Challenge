#import dependencies
import csv
import collections
from collections import Counter
import os

#Set the path for the csv file
#election_data_csv = "Resources/election_data.csv"
election_data_csv = os.path.join('Resources','election_data.csv')


#Initialize variable to hold data
Candidates=[]
Candidate_Votes=[]

#open and read the csv file
with open (election_data_csv, 'r') as cvsfile:
    Pypoll_csv_reader = csv.reader(cvsfile, delimiter=",")
    header = next(Pypoll_csv_reader) #<----identifies the first row as a "header" then moves to the next line.

#instructions for the row after header.
    for row in Pypoll_csv_reader:
        Candidates.append(row[2])  

Candidate_Count= Counter(Candidates) 

Candidate_Votes.append(Candidate_Count.most_common()) 


#return individual items in the list of (Candidate_Votes)
for item in Candidate_Votes:

    #[list number (negative goes backward) table only has 3 items] .3f = %
    #votes per candidates (divided by) total count of votes

    first= format((item[-3][1])*100/(sum(Candidate_Count.values())),'.3f')
    second= format((item[-2][1])*100/(sum(Candidate_Count.values())),'3f')
    third= format((item[-1][1])*100/(sum(Candidate_Count.values())),'3f')

    print("Election Results")
    print('--------------------------------------')
    print(f"Total Votes: {sum(Candidate_Count.values())}")
    print ('--------------------------------------')
    #candidate placement is off order to replicate the analysis results from UTA_Bootcamp_Module3
    print(f"{Candidate_Votes[0][-2][0]}: {second}% ({Candidate_Votes[0][-2][1]})")
    print(f"{Candidate_Votes[0][-3][0]}: {first}% ({Candidate_Votes[0][-3][1]})")
    print(f"{Candidate_Votes[0][-1][0]}: {third}% ({Candidate_Votes[0][-1][1]})")
    print('--------------------------------------')
    print(f"Winner: {Candidate_Votes[0][0][0]}")
    print('--------------------------------------')

    #creating and printing new file in a different folder
    Output_txt= os.path.join('analysis','output.txt')
    with open (Output_txt,'w') as file:
        file.write("Election Results"+"\n")
        file.write('-------------------------------------'+"\n")
        file.write(f"Total Votes: {sum(Candidate_Count.values())}"+"\n")
        file.write('--------------------------------------'+"\n")
        file.write(f"{Candidate_Votes[0][-2][0]}: {second}% ({Candidate_Votes[0][-2][1]})"+"\n")
        file.write(f"{Candidate_Votes[0][-3][0]}: {first}% ({Candidate_Votes[0][-3][1]})"+"\n")
        file.write(f"{Candidate_Votes[0][-1][0]}: {third}% ({Candidate_Votes[0][-1][1]})"+"\n")
        file.write('--------------------------------------'+"\n")
        file.write(f"Winner: {Candidate_Votes[0][0][0]}"+"\n")
        file.write('--------------------------------------'+"\n")
        

