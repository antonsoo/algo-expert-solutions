def tournamentWinner(competitions, results):
	# O(N) time, O(N) space
	
    teams = {}
	# populate the teams dictionary with losers and winners
	# I added continue each time to speed up the code a little
	# += 3 because we were told points increment by 3
	for i in range(len(results)):
		if results[i] == 1 and competitions[i][0] in teams: # home team won
			teams[competitions[i][0]] += 3 
			continue 
		if results[i] == 0 and competitions[i][1] in teams: # away-team won
			teams[competitions[i][1]] += 3
			continue
		if results[i] == 1 and competitions[i][0] not in teams:  # home team won
			teams[competitions[i][0]] = 3 # add the home-team that won
			teams[competitions[i][1]] = 0 # add the away-team that lost
			continue
		if results[i] == 0 and competitions[i][1] not in teams: # away-team won
			teams[competitions[i][0]] = 0 # # add the home-team that lost
			teams[competitions[i][1]] = 3 # add the away-team that won
			continue
	
	# find the maximum
	maxi = ("", 0)
	for key, val in teams.items():
		if val > maxi[1]:
			maxi = (key, val)
    return maxi[0]
