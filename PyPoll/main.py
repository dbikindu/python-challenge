import os
import csv

mypath = 'C:/Users/dbik/Documents/GitHub/Resources'

ElectionCSV = os.path.join(mypath, 'election_data.csv')

with open(ElectionCSV, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    header = next(csvreader)
    votes_cast = 0
    candidate = set()
    vote_khan = 0
    vote_correy = 0
    vote_li = 0
    vote_tooley = 0

    for vote in csvreader:
        votes_cast += 1

        candidate.add(vote[2])

        if (vote[2] == "Khan"):
            vote_khan += 1
        elif (vote[2] == "Correy"):
            vote_correy += 1
        elif (vote[2] == "Li"):
            vote_li += 1
        else:
            vote_tooley += 1

    percent_khan = (vote_khan / votes_cast)
    percent_correy = vote_correy / votes_cast
    percent_li = vote_li / votes_cast
    percent_tooley = vote_tooley / votes_cast

    # Find the winner of the election based on popular vote
    candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
    votes = [vote_khan, vote_correy, vote_li, vote_tooley]

    vote_cast_dict = dict(zip(candidate_list, votes))
    key = max(vote_cast_dict, key=vote_cast_dict.get)


    print("Election Results")
    print("---------------------")
    print("Total Votes: " + str(votes_cast))
    print("---------------------")
    print("Khan: " + "{:.3%}".format(percent_khan) + " " + (str(vote_khan)))
    print("Correy: " + "{:.3%}".format(percent_correy) + " " + (str(vote_correy)))
    print("Li: " + "{:.3%}".format(percent_li) + " " + (str(vote_li)))
    print("O'Tooley: " + "{:.3%}".format(percent_tooley) + " " + (str(vote_tooley)))
    print("---------------------")
    print("Winner: " + key)
    print("---------------------")

#  Export a text file with the results

result_file = 'C:/Users/dbik/Documents/GitHub/python-challenge/PyPoll/Summary_Election.txt'

with open(result_file, 'w') as file:
    file.write("Election Results")
    file.write("\n")
    file.write("---------------------")
    file.write("\n")
    file.write("Total Votes: " + str(votes_cast))
    file.write("\n")
    file.write("---------------------")
    file.write("\n")
    file.write("Khan: " + "{:.3%}".format(percent_khan) + " " + (str(vote_khan)))
    file.write("\n")
    file.write("Correy: " + "{:.3%}".format(percent_correy) + " " + (str(vote_correy)))
    file.write("\n")
    file.write("Li: " + "{:.3%}".format(percent_li) + " " + (str(vote_li)))
    file.write("\n")
    file.write("O'Tooley: " + "{:.3%}".format(percent_tooley) + " " + (str(vote_tooley)))
    file.write("\n")
    file.write("---------------------")
    file.write("\n")
    file.write("Winner: " + key)
    file.write("\n")
    file.write("---------------------")