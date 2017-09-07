import csv

with open("soccer_players.csv", newline="") as csvfile:
	teamreader = csv.reader(csvfile, delimiter="|")
	rows = list(teamreader)
	for row in rows[:]:
		print(", ".join(row))

#def bulid_league(team):
#	# open file
#	with open("teams.txt", "a") as file:
#		# write to the file
#		file.write(team)
#
#if __name__ == "__main__":
#	pass
#
#def player_letters(letter):
