# Ryan McNamara
"""This program uses available data from either moneypuck.com and nhl.com to
calculate the NHL player's expected fantasy points and compare with their
cost on a fantasy line up on FanDuel. For this first iteration I will use
exact stats to calculate the estimated fantasy points. I hope to later use
Money Puck's different stats that to calculate to not use and previous
stats but only future estimated."""

print("Hello and welcome to my fantasy point calculator for the NHL!", end=' ')
print("This is meant for use on FanDuel fantasy line ups")
print("First, lets calculate the average cost a player or goalie can be on "
      "your line up.")


def average_per_player(cost, players):
    """
This function calculates the average amount you can spend for each player on
your lineup.
    :param cost: How much you have to spend
    :param players: How many players you need
    """
    # Calculating the average and rounding down
    average_cost = ((cost // players) // 100) * 100
    # Calculating how much is left over if using that average
    left_over = (((cost // players) % 100) * players) + (cost % players)
    print("You can spend $", format(average_cost, "0.2f"), " on each of the ",
          players, " players with ",
          format(left_over, "0.2f"), " extra.", sep="")


def main():
    """
This is the main function that creates the fantasy lineup based on
user inputs.
    """
    total_cost = int(input(
        "Enter the amount of money you have to use (FanDuel is 55000): "))
    number_of_players = int(input(
        "Enter the number of players needed for your line up (FanDuel is 9): "
    ))
    average_per_player(total_cost, number_of_players)

    # The usual FanDuel line up has 2 centers, 2 wingers, 2 defensemen,
    # 2 utility player (free choice), and a goalie.
    center = 2
    winger = 2
    defense = 2
    utility = 2
    goalie = 1
    # This will collect all the player's expected points and add them up.
    total_expected = 0
    # This will collect all the player's names and display at the end.
    line_up = []
    total_players = 0
    line_up_cost = 0

    while total_players < number_of_players:
        if line_up_cost <= total_cost:
            print(
                "If you would like to calculate a Center's expected fantasy "
                "points, type 'Center'")
            print(
                "If you would like to calculate a Winger's expected fantasy "
                "points, type 'Winger'")
            print(
                "If you would like to calculate a Defensemen's expected "
                "fantasy points, type 'Defense'")
            print(
                "If you would like to calculate an extra Player's expected "
                "fantasy points, type 'Utility'")
            print(
                "If you would like to calculate a Goalie's expected fantasy "
                "points, type 'Goalie'")
            # A player and goalie will have different calculations for
            # fantasy points, thus if and elif between the two.
            position = input()

            if position == "Center":
                if center != 0:
                    print(
                        "Please utilize moneypuck.com/stats.htm to enter "
                        "requested data")
                    print(
                        "If you are not using moneypuck.com, enter values "
                        "within the range printed before the input.")
                    player_name = input("Please enter the Player's name: ")

                    if player_name == "Kirill Kaprisov":
                        # This is to show string multiplication but also my
                        # favorite hockey player is Kaprisov
                        print("KIRILL THE THRILL" * 10)

                    else:
                        # The next three lines of code calculate the players
                        # average minutes on the ice per game
                        print("The next value is usually from 100 to 1000")
                        icetime = int(input(
                            "Please enter the player's Icetime in minutes: "))
                        print("The next value is usually from 30 to 50")
                        games_played = int(
                            input("Please enter the player's Games Played: "))
                        icetime_per_game = icetime / games_played

                        # On FanDuel you gain points for shots, blocked
                        # shots, assists, and goals The next three lines of
                        # code calculate the players average shots per game
                        print("The next value is usually from 50 to 200")
                        shots_on_goal = float(
                            input("Please enter the player's Shots on Goal: "))
                        shots_per_minute = shots_on_goal / icetime
                        shots_per_game = shots_per_minute * icetime_per_game

                        # The next three lines of code calculate the amount
                        # of shots the opponents may block per game
                        print("The next value is usually from 300 to 600")
                        shots_blocked_team = float(input(
                            "Please enter the opponent team's shots blocked: "
                        ))
                        print("The next value is usually from 2000 to 3000")
                        teams_icetime = float(input(
                            "Please enter the opponent team's Icetime: "))
                        shots_blocked_team_per_minute = shots_blocked_team / \
                            teams_icetime
                        defense_on_player_shots = \
                            shots_blocked_team_per_minute * icetime_per_game
                        # Players average shots minus opponents average
                        # blocked shots
                        shots_expected = shots_per_game - \
                            defense_on_player_shots
                        # On FanDuel, each shot is worth 1.6 points
                        points_from_shots = 1.6 * shots_expected

                        # The next three lines of code calculate the players
                        # average blocked shots per game
                        print("The next value is usually from 10 to 100")
                        shots_blocked = float(
                            input("Please enter the player's Shots Blocked: "))
                        shot_blocks_per_minute = shots_blocked / icetime
                        shot_blocks_per_game = shot_blocks_per_minute * \
                            icetime_per_game
                        # On FanDuel, each blocked shot is worth 1.6 points
                        points_from_blocks = 1.6 * shot_blocks_per_game

                        # The next three lines of code calculate the players
                        # average assists per game
                        print("The next value is usually from 0 to 50")
                        assists = float(
                            input("Please enter the player's assists: "))
                        assists_per_minute = assists / icetime
                        assists_per_game = assists_per_minute * \
                            icetime_per_game
                        # On FanDuel, each assist is worth 8 points
                        points_from_assists = 8 * assists_per_game

                        # The next three lines of code calculate the players
                        # average goals per game
                        print("The next value is usually from 0 to 50")
                        goals = float(
                            input("Please enter the player's goals: "))
                        goals_per_minute = goals / icetime
                        goals_per_game = goals_per_minute * icetime_per_game

                        # The next three lines of code calculate the
                        # opponents average goals defended per game
                        print("The next value is usually from -50 to 50")
                        goals_against_below_expected = float(
                            input(
                                "Please enter the player's opponents Goals "
                                "Against Above Expected: "))
                        goals_defended_per_minute = \
                            goals_against_below_expected / teams_icetime
                        defense_on_player_goals = goals_defended_per_minute \
                            * icetime_per_game

                        # Players average goals minus opponents average
                        # goals defended
                        goals_expected = goals_per_game \
                            + defense_on_player_goals
                        # On FanDuel, each goal is 12 points
                        points_from_goals = 12 * goals_expected

                        # Adding up all expected points
                        total_points = points_from_shots + \
                            points_from_blocks + \
                            points_from_assists + points_from_goals
                        print("The player's expected fantasy points is ",
                              format(total_points, "0.2f"), sep="")
                        print("The next value is usually from 3000 to 10500")
                        cost = float(input(
                            "Please enter the cost of the player on FanDuel: "
                        ))

                        # This is how FanDuel determines the value of a
                        # player after a game has been completed
                        value = (total_points / cost) * 1000
                        # Preparing for string addition
                        cost_string = str(format(cost, "0.0f"))
                        value_string = str(format(value, "0.2f"))

                        if value >= 1.5:
                            print(
                                player_name + " is worth their price of $" +
                                cost_string + "as they have an estimated "
                                              "value of " + value_string)
                        else:
                            print(
                                Player_Name + " is not worth their price of $"
                                + cost_string + "as they have an estimated "
                                                "value of " + value_string)

                        print(
                            "If you would like to add this player to your "
                            "line up, type YES. If not, type anything else")
                        selection = input()

                        if selection == "YES":
                            center -= 1
                            line_up.append(player_name)
                            total_expected += total_points
                            total_players += 1
                            line_up_cost += cost
                            if total_players < 9:
                                average_remaining = (
                                                            total_cost -
                                                            line_up_cost) / (
                                                            number_of_players
                                                            - total_players)
                                average_string = str(
                                    format(average_remaining, "0.2f"))
                                print(
                                    "This player was added to your line up "
                                    "and you have " + average_string + "left "
                                                                       "for "
                                                                       "each "
                                                                       "remain"
                                                                       "ing "
                                                                       "playe"
                                                                       "r.")
                            else:
                                print("You have completed your line up!")
                        else:
                            print("The player was not added.")
                else:
                    print(
                        "You already have too many players in this category, "
                        "please pick a different player type.")

            elif position == "Winger":
                if winger != 0:
                    print(
                        "Please utilize moneypuck.com/stats.htm to enter "
                        "requested data")
                    print(
                        "If you are not using moneypuck.com, enter values "
                        "within the range printed before the input.")
                    player_name = input("Please enter the Player's name: ")

                    if player_name == "Kirill Kaprisov":
                        # This is to show string multiplication but also my
                        # favorite hockey player is Kaprisov
                        print("KIRILL THE THRILL" * 10)

                    else:
                        # The next three lines of code calculate the players
                        # average minutes on the ice per game
                        print("The next value is usually from 100 to 1000")
                        icetime = int(input(
                            "Please enter the player's Icetime in minutes: "))
                        print("The next value is usually from 30 to 50")
                        games_played = int(
                            input("Please enter the player's Games Played: "))
                        icetime_per_game = icetime / games_played

                        # On FanDuel you gain points for shots, blocked
                        # shots, assists, and goals The next three lines of
                        # code calculate the players average shots per game
                        print("The next value is usually from 50 to 200")
                        shots_on_goal = float(
                            input("Please enter the player's Shots on Goal: "))
                        shots_per_minute = shots_on_goal / icetime
                        shots_per_game = shots_per_minute * icetime_per_game

                        # The next three lines of code calculate the amount
                        # of shots the opponents may block per game
                        print("The next value is usually from 300 to 600")
                        shots_blocked_team = float(input(
                            "Please enter the opponent team's "
                            "shots blocked: "))
                        print("The next value is usually from 2000 to 3000")
                        teams_icetime = float(input(
                            "Please enter the opponent team's Icetime: "))
                        shots_blocked_team_per_minute = shots_blocked_team / \
                            teams_icetime
                        defense_on_player_shots = \
                            shots_blocked_team_per_minute * icetime_per_game
                        # Players average shots minus opponents average
                        # blocked shots
                        shots_expected = shots_per_game - \
                            defense_on_player_shots
                        # On FanDuel, each shot is worth 1.6 points
                        points_from_shots = 1.6 * shots_expected

                        # The next three lines of code calculate the players
                        # average blocked shots per game
                        print("The next value is usually from 10 to 100")
                        shots_blocked = float(
                            input("Please enter the player's Shots Blocked: "))
                        shot_blocks_per_minute = shots_blocked / icetime
                        shot_blocks_per_game = shot_blocks_per_minute * \
                            icetime_per_game
                        # On FanDuel, each blocked shot is worth 1.6 points
                        points_from_blocks = 1.6 * shot_blocks_per_game

                        # The next three lines of code calculate the players
                        # average assists per game
                        print("The next value is usually from 0 to 50")
                        assists = float(
                            input("Please enter the player's assists: "))
                        assists_per_minute = assists / icetime
                        assists_per_game = assists_per_minute * \
                            icetime_per_game
                        # On FanDuel, each assist is worth 8 points
                        points_from_assists = 8 * assists_per_game

                        # The next three lines of code calculate the players
                        # average goals per game
                        print("The next value is usually from 0 to 50")
                        goals = float(
                            input("Please enter the player's goals: "))
                        goals_per_minute = goals / icetime
                        goals_per_game = goals_per_minute * icetime_per_game

                        # The next three lines of code calculate the
                        # opponents average goals defended per game
                        print("The next value is usually from -50 to 50")
                        goals_against_below_expected = float(
                            input(
                                "Please enter the player's opponents Goals "
                                "Against Above Expected: "))
                        goals_defended_per_minute = \
                            goals_against_below_expected / teams_icetime
                        defense_on_player_goals = goals_defended_per_minute \
                            * icetime_per_game

                        # Players average goals minus opponents average
                        # goals defended
                        goals_expected = goals_per_game + \
                            defense_on_player_goals
                        # On FanDuel, each goal is 12 points
                        points_from_goals = 12 * goals_expected

                        # Adding up all expected points
                        total_points = points_from_shots + points_from_blocks \
                            + points_from_assists + \
                            points_from_goals
                        print("The player's expected fantasy points is ",
                              format(total_points, "0.2f"), sep="")
                        print("The next value is usually from 3000 to 10500")
                        cost = float(input(
                            "Please enter the cost of the player on FanDuel: "
                        ))

                        # This is how FanDuel determines the value of a
                        # player after a game has been completed
                        value = (total_points / cost) * 1000
                        # Preparing for string addition
                        cost_string = str(format(cost, "0.0f"))
                        value_string = str(format(value, "0.2f"))

                        if value >= 1.5:
                            print(
                                player_name + " is worth their price of $" +
                                cost_string + "as they have an estimated "
                                              "value of " + value_string)
                        else:
                            print(
                                player_name + " is not worth their price of $"
                                + cost_string + "as they have an estimated "
                                                "value of " + value_string)

                        print(
                            "If you would like to add this player to your "
                            "line up, type YES. If not, type anything else")
                        selection = input()

                        if selection == "YES":
                            winger -= 1
                            line_up.append(player_name)
                            total_expected += total_points
                            total_players += 1
                            line_up_cost += cost
                            if total_players < 9:
                                average_remaining = (
                                                            total_cost -
                                                            line_up_cost) / (
                                                            number_of_players
                                                            - total_players)
                                average_string = str(
                                    format(average_remaining, "0.2f"))
                                print(
                                    "This player was added to your line up "
                                    "and you have " + average_string + "left "
                                                                       "for "
                                                                       "each "
                                                                       "remain"
                                                                       "ing "
                                                                       "playe"
                                                                       "r.")
                            else:
                                print("You have completed your line up!")
                        else:
                            print("The player was not added.")
                else:
                    print(
                        "You already have too many players in this category, "
                        "please pick a different player type.")

            elif position == "Defense":
                if defense != 0:
                    print(
                        "Please utilize moneypuck.com/stats.htm to enter "
                        "requested data")
                    print(
                        "If you are not using moneypuck.com, enter values "
                        "within the range printed before the input.")
                    player_name = input("Please enter the Player's name: ")

                    if player_name == "Kirill Kaprisov":
                        # This is to show string multiplication but also my
                        # favorite hockey player is Kaprisov
                        print("KIRILL THE THRILL" * 10)

                    else:
                        # The next three lines of code calculate the players
                        # average minutes on the ice per game
                        print("The next value is usually from 100 to 1000")
                        icetime = int(input(
                            "Please enter the player's Icetime in minutes: "))
                        print("The next value is usually from 30 to 50")
                        games_played = int(
                            input("Please enter the player's Games Played: "))
                        icetime_per_game = icetime / games_played

                        # On FanDuel you gain points for shots, blocked
                        # shots, assists, and goals The next three lines of
                        # code calculate the players average shots per game
                        print("The next value is usually from 50 to 200")
                        shots_on_goal = float(
                            input("Please enter the player's Shots on Goal: "))
                        shots_per_minute = shots_on_goal / icetime
                        shots_per_game = shots_per_minute * icetime_per_game

                        # The next three lines of code calculate the amount
                        # of shots the opponents may block per game
                        print("The next value is usually from 300 to 600")
                        shots_blocked_team = float(input(
                            "Please enter the opponent team's shots blocked: "
                        ))
                        print("The next value is usually from 2000 to 3000")
                        teams_icetime = float(input(
                            "Please enter the opponent team's Icetime: "))
                        shots_blocked_team_per_minute = shots_blocked_team / \
                            teams_icetime
                        defense_on_player_shots = \
                            shots_blocked_team_per_minute * icetime_per_game
                        # Players average shots minus opponents average
                        # blocked shots
                        shots_expected = shots_per_game - \
                            defense_on_player_shots
                        # On FanDuel, each shot is worth 1.6 points
                        points_from_shots = 1.6 * shots_expected

                        # The next three lines of code calculate the players
                        # average blocked shots per game
                        print("The next value is usually from 10 to 100")
                        shots_blocked = float(
                            input("Please enter the player's Shots Blocked: "))
                        shot_blocks_per_minute = shots_blocked / Icetime
                        shot_blocks_per_game = shot_blocks_per_minute * \
                            icetime_per_game
                        # On FanDuel, each blocked shot is worth 1.6 points
                        points_from_blocks = 1.6 * shot_blocks_per_game

                        # The next three lines of code calculate the players
                        # average assists per game
                        print("The next value is usually from 0 to 50")
                        assists = float(
                            input("Please enter the player's assists: "))
                        assists_per_minute = assists / Icetime
                        assists_per_game = assists_per_minute * \
                            icetime_per_game
                        # On FanDuel, each assist is worth 8 points
                        points_from_assists = 8 * assists_per_game

                        # The next three lines of code calculate the players
                        # average goals per game
                        print("The next value is usually from 0 to 50")
                        goals = float(
                            input("Please enter the player's goals: "))
                        goals_per_minute = goals / Icetime
                        goals_per_game = goals_per_minute * icetime_per_game

                        # The next three lines of code calculate the
                        # opponents average goals defended per game
                        print("The next value is usually from -50 to 50")
                        goals_against_below_expected = float(
                            input(
                                "Please enter the player's opponents Goals "
                                "Against Above Expected: "))
                        goals_defended_per_minute = \
                            goals_against_below_expected / teams_icetime
                        defense_on_player_goals = goals_defended_per_minute * \
                            icetime_per_game

                        # Players average goals minus opponents average
                        # goals defended
                        goals_expected = goals_per_game + \
                            defense_on_player_goals
                        # On FanDuel, each goal is 12 points
                        points_from_goals = 12 * goals_expected

                        # Adding up all expected points
                        total_points = points_from_shots + points_from_blocks
                        + points_from_assists + points_from_goals
                        print("The player's expected fantasy points is ",
                              format(total_points, "0.2f"), sep="")
                        print("The next value is usually from 3000 to 10500")
                        cost = float(input(
                            "Please enter the cost of the player on FanDuel: "
                        ))

                        # This is how FanDuel determines the value of a
                        # player after a game has been completed
                        value = (total_points / cost) * 1000
                        # Preparing for string addition
                        cost_string = str(format(cost, "0.0f"))
                        value_string = str(format(value, "0.2f"))

                        if value >= 1.5:
                            print(
                                player_name + " is worth their price of $" +
                                cost_string + "as they have an estimated "
                                              "value of " + value_string)
                        else:
                            print(
                                player_name + " is not worth their price of $"
                                + cost_string + "as they have an estimated "
                                                "value of " + value_string)

                        print(
                            "If you would like to add this player to your "
                            "line up, type YES. If not, type anything else")
                        selection = input()

                        if selection == "YES":
                            defense -= 1
                            line_up.append(player_name)
                            total_expected += total_points
                            total_players += 1
                            line_up_cost += cost
                            if total_players < 9:
                                average_remaining = (
                                                            total_cost -
                                                            line_up_cost) / (
                                                            number_of_players
                                                            - total_players)
                                average_string = str(
                                    format(average_remaining, "0.2f"))
                                print(
                                    "This player was added to your line up "
                                    "and you have " + average_string + "left "
                                                                       "for "
                                                                       "each "
                                                                       "rema"
                                                                       "ining "
                                                                       "playe"
                                                                       "r.")
                            else:
                                print("You have completed your line up!")
                        else:
                            print("The player was not added.")
                else:
                    print(
                        "You already have too many players in this category, "
                        "please pick a different player type.")

            elif position == "Utility":
                if (center != 0) or (winger != 0) or (defense != 0) or (
                        goalie != 0):
                    print(
                        "I would suggest filling out other roles before "
                        "picking Utility Players")

                elif utility != 0:
                    print(
                        "Please utilize moneypuck.com/stats.htm to enter "
                        "requested data")
                    print(
                        "If you are not using moneypuck.com, enter values "
                        "within the range printed before the input.")
                    player_name = input("Please enter the Player's name: ")

                    if player_name == "Kirill Kaprisov":
                        # This is to show string multiplication but also my
                        # favorite hockey player is Kaprisov
                        print("KIRILL THE THRILL" * 10)

                    else:
                        # The next three lines of code calculate the players
                        # average minutes on the ice per game
                        print("The next value is usually from 100 to 1000")
                        icetime = int(input(
                            "Please enter the player's Icetime in minutes: "))
                        print("The next value is usually from 30 to 50")
                        games_played = int(
                            input("Please enter the player's Games Played: "))
                        icetime_per_game = icetime / games_played

                        # On FanDuel you gain points for shots, blocked
                        # shots, assists, and goals The next three lines of
                        # code calculate the players average shots per game
                        print("The next value is usually from 50 to 200")
                        shots_on_goal = float(
                            input("Please enter the player's Shots on Goal: "))
                        shots_per_minute = shots_on_goal / icetime
                        shots_per_game = shots_per_minute * icetime_per_game

                        # The next three lines of code calculate the amount
                        # of shots the opponents may block per game
                        print("The next value is usually from 300 to 600")
                        shots_blocked_team = float(input(
                            "Please enter the opponent team's shots blocked: ")
                        )
                        print("The next value is usually from 2000 to 3000")
                        teams_icetime = float(input(
                            "Please enter the opponent team's Icetime: "))
                        shots_blocked_team_per_minute = shots_blocked_team / \
                            teams_icetime
                        defense_on_player_shots = \
                            shots_blocked_team_per_minute * icetime_per_game
                        # Players average shots minus opponents average
                        # blocked shots
                        shots_expected = shots_per_game - \
                            defense_on_player_shots
                        # On FanDuel, each shot is worth 1.6 points
                        points_from_shots = 1.6 * shots_expected

                        # The next three lines of code calculate the players
                        # average blocked shots per game
                        print("The next value is usually from 10 to 100")
                        shots_blocked = float(
                            input("Please enter the player's Shots Blocked: "))
                        shot_blocks_per_minute = shots_blocked / Icetime
                        shot_blocks_per_game = shot_blocks_per_minute * \
                            icetime_per_game
                        # On FanDuel, each blocked shot is worth 1.6 points
                        points_from_blocks = 1.6 * shot_blocks_per_game

                        # The next three lines of code calculate the players
                        # average assists per game
                        print("The next value is usually from 0 to 50")
                        assists = float(
                            input("Please enter the player's assists: "))
                        assists_per_minute = assists / Icetime
                        assists_per_game = assists_per_minute * \
                            icetime_per_game
                        # On FanDuel, each assist is worth 8 points
                        points_from_assists = 8 * assists_per_game

                        # The next three lines of code calculate the players
                        # average goals per game
                        print("The next value is usually from 0 to 50")
                        goals = float(
                            input("Please enter the player's goals: "))
                        goals_per_minute = goals / Icetime
                        goals_per_game = goals_per_minute * icetime_per_game

                        # The next three lines of code calculate the
                        # opponents average goals defended per game
                        print("The next value is usually from -50 to 50")
                        goals_against_below_expected = float(
                            input(
                                "Please enter the player's opponents Goals "
                                "Against Above Expected: "))
                        goals_defended_per_minute = \
                            goals_against_below_expected / teams_icetime
                        defense_on_player_goals = goals_defended_per_minute * \
                            icetime_per_game

                        # Players average goals minus opponents average
                        # goals defended
                        goals_expected = goals_per_game + \
                            defense_on_player_goals
                        # On FanDuel, each goal is 12 points
                        points_from_goals = 12 * goals_expected

                        # Adding up all expected points
                        total_points = points_from_shots + points_from_blocks \
                            + points_from_assists + \
                            points_from_goals
                        print("The player's expected fantasy points is ",
                              format(total_points, "0.2f"), sep="")
                        print("The next value is usually from 3000 to 10500")
                        cost = float(input(
                            "Please enter the cost of the player on FanDuel: "
                        ))

                        # This is how FanDuel determines the value of a
                        # player after a game has been completed
                        value = (total_points / cost) * 1000
                        # Preparing for string addition
                        cost_string = str(format(cost, "0.0f"))
                        value_string = str(format(value, "0.2f"))

                        if value >= 1.5:
                            print(
                                player_name + " is worth their price of $"
                                + cost_string + "as they have an estimated "
                                                "value of " + value_string)
                        else:
                            print(
                                player_name + " is not worth their price of $"
                                + cost_string + "as they have an estimated "
                                                "value of " + value_string)

                        print(
                            "If you would like to add this player to your "
                            "line up, type YES. If not, type anything else")
                        selection = input()

                        if selection == "YES":
                            utility -= 1
                            line_up.append(player_name)
                            total_expected = total_expected + total_points
                            total_players += 1
                            line_up_cost += cost
                            if total_players < 9:
                                average_remaining = (
                                                            total_cost -
                                                            line_up_cost) / (
                                                            number_of_players
                                                            - total_players)
                                average_string = str(
                                    format(average_remaining, "0.2f"))
                                print(
                                    "This player was added to your line up "
                                    "and you have " + average_string + "left "
                                                                       "for "
                                                                       "each "
                                                                       "remain"
                                                                       "ing "
                                                                       "playe"
                                                                       "r.")
                            else:
                                print("You have completed your line up!")
                        else:
                            print("The player was not added.")
                else:
                    print(
                        "You already have too many players in this category, "
                        "please pick a different player type.")

            elif position == "Goalie":
                if goalie != 0:
                    print(
                        "Please utilize moneypuck.com/stats.htm to enter "
                        "requested data")
                    print(
                        "If you are not using moneypuck.com, enter values "
                        "within the range printed before the input.")
                    player_name = input("Please enter the Goalie's name: ")

                    if player_name == "Kirill Kaprisov":
                        # This is to show string multiplication but also my
                        # favorite hockey player is Kaprisov
                        print("KIRILL THE THRILL" * 10)

                    else:
                        # The next four lines of code calculate the goalie's
                        # average goals against for the game
                        print("The next value is usually from 1.00 to 4.00")
                        goals_against_average = float(input(
                            "Please enter the goalie's goals "
                            "against average: "))
                        print("The next value is usually from 100 to 200")
                        opponents_goals_for = float(input(
                            "Please enter the opponent's total goals for: "))
                        print("The next value is usually from 40 to 50")
                        opponents_games_played = float(input(
                            "Please enter the number of games the opponent "
                            "has played: "))
                        opponents_goals_per_game = opponents_goals_for / \
                            opponents_games_played

                        # Taking the average of goalie's goals against and
                        # opponents goals for
                        expected_goals_against = (goals_against_average +
                                                  opponents_goals_per_game) / 2
                        # Each goal against is minus 4 points, so we will
                        # subtract this value later
                        points_from_goals_against = 4 * expected_goals_against

                        # The next three lines of code calculate the
                        # goalie's saves per game
                        print("The next value is usually from 1000 to 2000")
                        opponents_shots = float(
                            input("Please enter the opponent's total shots: "))
                        opponents_shots_per_game = opponents_shots / \
                            opponents_games_played
                        # Opponents shots minus goals scored equals goalie's
                        # saves
                        goalies_expected_saves = opponents_shots_per_game - \
                            expected_goals_against
                        # On FanDuel, each save is 0.8 points
                        points_from_saves = 0.8 * goalies_expected_saves

                        # Teams Win Probability Since this really has
                        # nothing to do with the goalie but gives the goalie
                        # points, I am just using the win probability
                        print("The next value is usually from 0.000 to 1.000")
                        teams_win_probability = float(input(
                            "Please enter the teams win probability in "
                            "decimal form: "))
                        # On FanDuel, a win is 12 points
                        points_from_win = 12 * teams_win_probability

                        # Shutout Probability (Goalie lets in no goals)
                        print("The next value is usually from 0.700 to 1.000")
                        save_percentage = float(input(
                            "Please enter the goalie's save percentage in "
                            "decimal form: "))
                        # A goalie can be very good on average, usually
                        # shown by save percentage rather than goals against
                        # average Multiplied by opponents shots to get
                        # estimated goals against
                        possible_goals_against = opponents_goals_per_game * \
                            save_percentage
                        # An estimate on the probability of saving those
                        # expected goals against
                        shutout_probability = (1 / possible_goals_against) ** 2
                        # On FanDuel, a shutout is 8 points
                        points_from_shutout = 8 * shutout_probability

                        # Adding up all expected points and subtracting the
                        # points from goals against
                        total_points = points_from_saves + points_from_win + \
                            points_from_shutout - \
                            points_from_goals_against
                        print("The goalie's expected fantasy points is ",
                              format(total_points, "0.2f"), sep="")
                        print("The next value is usually from 3500 to 10500")
                        cost = float(input(
                            "Please enter the cost of the goalie on FanDuel: "
                        ))

                        # This is how FanDuel determines the value of a
                        # player after a game has been completed
                        value = (total_points / cost) * 1000
                        # Preparing for string addition
                        cost_string = str(format(cost, "0.0f"))
                        value_string = str(format(value, "0.2f"))
                        if value >= 1.5:
                            print(
                                player_name + " is worth their price of $" +
                                cost_string + "as they have an estimated "
                                              "value of " + value_string)
                        else:
                            print(
                                player_name + " is not worth their price of $"
                                + cost_string + "as they have an estimated "
                                                "value of " + value_string)

                        print(
                            "If you would like to add this player to your "
                            "line up, type YES. If not, type anything else")
                        selection = input()

                        if selection == "YES":
                            goalie -= 1
                            line_up.append(player_name)
                            total_expected += total_points
                            total_players += 1
                            line_up_cost += cost
                            if Total_Players < 9:
                                average_remaining = (
                                                            total_cost -
                                                            line_up_cost) / (
                                                            number_of_players
                                                            - total_players)
                                average_string = str(
                                    format(average_remaining, "0.2f"))
                                print(
                                    "This player was added to your line up "
                                    "and you have " + average_string + "left "
                                                                       "for "
                                                                       "each "
                                                                       "remain"
                                                                       "ing "
                                                                       "playe"
                                                                       "r.")
                            else:
                                print("You have completed your line up!")
                        else:
                            print("The player was not added.")
                else:
                    print(
                        "You already have too many players in this category, "
                        "please pick a different player type.")
            else:
                print("Please type one of the options below.")
        else:
            print(
                "You have gone over budget, you have to restart and pick "
                "some cheaper players!")
            quit(main)
    print("Your line up is:")
    for x in range(len(line_up)):
        print(line_up[x])

    print("Your expected points are", total_expected)
    if not (total_Cost == line_up_cost):
        print(
            "You have money left over so it is possible to make a better "
            "line up.")


main()
print("Good Luck!")

# I didn't have anywhere to use AND so here it is
favorite_team = input("Who is your favorite hockey team?")
favorite_player = input("Who is your favorite player?")
if favorite_team == "Minnesota Wild" and favorite_player == "Kirill Kaprisov":
    print("Correct.")
elif favorite_team == "Minnesota Wild" or favorite_player == "Kirill Kaprisov":
    print("Almost.")
else:
    print("Wrong.")
