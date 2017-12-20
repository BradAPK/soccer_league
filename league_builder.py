import csv

# open 'soccer_players.csv'
def import_players( file, new_line, delimiter ):
    with open( file, newline=new_line ) as csvfile:
        file_reader = csv.DictReader( csvfile, delimiter=delimiter )
        players = list( file_reader )

        return players



# sort players into experienced and inexperienced
def sort_players( players ):
    experienced_players = []
    inexperienced_players = []

    for player in players:

        if player[ 'Soccer Experience' ] == 'YES':
            experienced_players.append( player )
        else:
            inexperienced_players.append( player )

    return experienced_players, inexperienced_players



# assign players to teams based on index
def assign_players( players, team_list ):
    index = 0
    sorted_players = sort_players( players )
    player_list = []
    teams = []

    for key, value in team_list.items():
        teams.append( key )

    for group in sorted_players:
        range = len( teams ) - 1

        for player in group:
            player[ 'Team' ] = teams[ index ]
            player_list.append( player )

            if index < range:
                index += 1
            else:
                index = 0

    return player_list



# make teams
def make_teams( team_list, player_list ):

    for player in player_list:
        team = player[ 'Team' ]

        if team in team_list:
            team_list[ team ].append( player )

    return team_list


# write teams to 'teams.txt'
def write_teams( teams ):
    file = open( 'teams.txt', 'a' )

    for team, players in teams.items():
        file.write( team + '\n' )

        for player in players:
            name = player[ 'Name' ]
            experience = player[ 'Soccer Experience' ]
            guardians = player[ 'Guardian Name(s)' ]

            file.write( "{}, {}, {}\n".format( name, experience, guardians ) )

        file.write( "\n" )


 
if __name__ == "__main__":
    imported_players = import_players( 'soccer_players.csv', '', ',' )

    team_list = { 'Sharks': [], 'Dragons': [], 'Raptors': [] }

    assigned_players = assign_players( imported_players, team_list )

    teams = make_teams( team_list, assigned_players )

    write_teams( teams )