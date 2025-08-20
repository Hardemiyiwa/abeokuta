voters = set()
# creating  slot available for voters
for x in range(1000):
    # collecting the user data
    voter_names = input("Enter your name (Enter \"done\" once to submit the all the vote): ").title().strip()
    if voter_names == "Done":
        break
    # avoiding double votes
    elif voter_names in voters:
        print(f"Warning, {voter_names} already had a vote")
    else:
        # adding the collection of votes
        voters.add(voter_names)
        print(f"\n{len(voters)} numbers of voters registered")