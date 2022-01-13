




# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save a file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter.
total_votes = 0

# Candidate Options and Candidate votes
candidate_options = []
candidate_votes = {}

# County names and County votes
county_names = []
county_votes = {}

# Begin tracking the winning candidate, vote count and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Challenges Track the largest county voter turnout and its percentage
largest_county_turnout = ""
largest_county_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header row.
    header = next(reader)

    # Print each row in the csv file.
    for row in reader:
        # Add to the total votes count.
        total_votes = total_votes + 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Extract the count name from each row
        county_name = row[1]

        # If the candidate does not match any existing candidate add it into
        # the list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Add begin tracking that candidate voter count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate count
        candidate_votes[candidate_name] += 1

        # Challenge count
        if county_name not in county_names:

            # Challenge add it to the list in running
            county_names.append(county_name)

            # tracking that candidate voter count
            county_votes[county_name] = 0
        county_votes[county_name] +=1

# Save the result to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vout count
    election_results = (
        f"\nElection Results"
        f"\n--------------------\n"
        f"Total Votes: {total_votes:,}"
        f"\n--------------------\n\n"
        f"County Votes:\n"
    )

    print(election_results, end="")
    txt_file.write(election_results)

    # Determine the percentage of votes for each county by looping through the county votes.
    for county in county_votes:
        # Retrieve vote count and percentage
        county_vote = county_votes[county]
        # Calculate the percentage of votes.
        county_percent = int(county_vote) / int(total_votes) * 100
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n"    
        )
        print(county_results, end="")
        txt_file.write(county_results)

        # Dermine winning vote count and candidate
        if(county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county
        # Print the county with the largest turnout
    largest_county_turnout = (
        f"\n-------------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------------\n"  
    )  
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    for candidate in candidate_votes:
        #Retrive vote count and percentage
        votes = candidate_votes[candidate]
        #Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )
        
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percentange =
            # vote_percentage.
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.

    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"----------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
