import os
import csv


total_votes = 0

votespercandidate = {}


electiondata_csv = os.path.join('Resources', 'election_data.csv')
with open(electiondata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader, None)
    
    for row in csvreader:
        total_votes += 1
        if row[2] not in votespercandidate:
            votespercandidate[row[2]] = 1
        else:
            votespercandidate[row[2]] += 1

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for candidate, votes in votespercandidate.items():
    print(candidate + ": " + "{:.2%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votespercandidate, key=votespercandidate.get)

print(f"Winner: {winner}")

output = os.path.join("Analysis", "election_file.txt")
with open(output, "w") as text:
    text.write("Election Results")
    text.write("\n")
    text.write(".......................................")
    text.write("\n")
    text.write("Total Vote: " + str(total_votes))
    text.write("\n")
    text.write(".......................................")
    text.write("\n")
    text.write("The winner is: " + winner)
    text.write("\n")
    text.write("........................................")      


   

















    




    

