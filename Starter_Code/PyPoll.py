import os
import csv

PyPoll_csvpath = os.path.join('Resources', "election_data.csv")
output_path = os.path.join('Pypoll_Output')

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Open and read the CSV file
with open(PyPoll_csvpath, newline='', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in the CSV file
    for row in csvreader:
        candidate_name = row[2]

        # Update total votes
        total_votes += 1

        # Update candidate votes
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

        # Update winner information
        if candidates[candidate_name] > winner["votes"]:
            winner["name"] = candidate_name
            winner["votes"] = candidates[candidate_name]

# Print the election results to the terminal
print("Election Results")
print("-" * 25)
print(f"Total Votes: {total_votes}")
print("-" * 25)

# Export the election results to a text file
with open(output_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-" * 25 + "\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-" * 25 + "\n")

    # Loop through candidates and print/write their results
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        # Update winner information
        if votes > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = votes

print("-" * 25)
print(f"Winner: {winner['name']}")
print("-" * 25)

# Export the winner information to a text file
with open(output_path, 'a') as output_file:
    output_file.write("-" * 25 + "\n")
    output_file.write(f"Winner: {winner['name']}\n")
    output_file.write("-" * 25 + "\n")
