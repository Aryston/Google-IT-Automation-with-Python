teams = ['Milan', 'Inter', 'Juventus', 'Roma']
for home_teams in teams:
    for away_teams in teams:
        if home_teams != away_teams:
            print(home_teams, "vs", away_teams)