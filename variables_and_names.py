#There are two empty lines in the code to segment the different parts (Variable Names, Variable Calculation, Variable Printing)

# The name of the team is being stored in the variable "team"
team = "Toronto Blue Jays"
# The current date is being stored in the variable "current_date"
current_date = "July 18, 2021"
# The player's name is being stored in the variable "player"
player = "Vladimir Guerrero Jr."
# The number of home runs hit so far by the player is being stored in the variable "home_runs_to_date"
home_runs_to_date = 31
# The number of games the player has played so far this season is stored in the variable "games_played"
games_played = 88
# The total number of games in the season is being stored in the variable "total_season_games"
total_season_games = 162
# The current MLB record for most home runs in a season is stored in the variable "home_run_record"
home_run_record = 73

# The remaining games in the season are calculated and stored in the variable "games_remaining"
# ASK TEACHER
games_remaining = total_season_games - games_played
# The average number of home runs per game is calculated and stored in the variable "home_runs_per_game"
home_runs_per_game = home_runs_to_date / games_played
# The projected number of home runs for the season is calculated and stored in the variable "projected_home_runs"
projected_home_runs = home_runs_per_game * total_season_games
# A boolean value indicating whether the player is on pace to break the home run record is stored in the variable "can_break_record"
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {round(home_runs_per_game,2)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs,2)} home runs this season.")