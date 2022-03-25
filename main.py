# Ryan McNamara
# This program uses avialable data from either moneypuck.com and nhl.com to calculate the NHL player's
# expected fantasy points and compare with their cost on a fantasy line up on FanDuel.
# For this first iteration I will use exact stats to caculate the estimated fantasy points.
# I hope to later use Money Puck's different stats that the calculate to not use and previous stats but only future estimated.

print("Hello and welcome to my fantasy point calculator for the NHL!", end=' ')
print("This is meant for use on FanDuel fantasy line ups")
print("First, lets calculate the average cost a player or goalie can be on your line up.")

def Average_Per_Player(Cost, Players):
    # Calculating the average and rounding down
    Average_Cost = ((Cost // Players) // 100) * 100
    # Calculating how much is left over if using that average
    Left_Over = (((Cost // Players) % 100) * Players) + (Cost % Players)
    print("You can spend $", format(Average_Cost, "0.2f"), " on each of the ", Players, " players with ",
          format(Left_Over, "0.2f"), " extra.", sep="")

def main():
    Total_Cost = int(input("Enter the amount of money you have to use (FanDuel is 55000): "))
    Number_Of_Players = int(input("Enter the number of players needed for your line up (FanDuel is 9): "))
    Average_Per_Player(Total_Cost, Number_Of_Players)

    # The usual FanDuel line up has 2 centers, 2 wingers, 2 defensemen, 2 utility player (free choice), and a goalie.
    Center = 2
    Winger = 2
    Defense = 2
    Utility = 2
    Goalie = 1
    #This will collect all the player's expected points and add them up.
    Total_Expected = 0
    #This will collect all the player's names and display at the end.
    Line_Up = []
    Total_Players = 0
    Line_Up_Cost = 0

    while Total_Players < Number_Of_Players:
        if Line_Up_Cost <= Total_Cost:
            print("If you would like to calculate a Center's expected fantasy points, type 'Center'")
            print("If you would like to calculate a Winger's expected fantasy points, type 'Winger'")
            print("If you would like to calculate a Defensemen's expected fantasy points, type 'Defense'")
            print("If you would like to calculate an extra Player's expected fantasy points, type 'Utility'")
            print("If you would like to calculate a Goalie's expected fantasy points, type 'Goalie'")
            # A player and goalie will have different calculations for fantasy points, thus if and elif between the two.
            Position = input()

            if Position == "Center":
                if Center != 0:
                    print("Please utilize moneypuck.com/stats.htm to enter requested data")
                    print("If you are not using moneypuck.com, enter values within the range printed before the input.")
                    Player_Name = input("Please enter the Player's name: ")

                    if (Player_Name == "Kirill Kaprisov"):
                        # This is to show string multiplication but also my favorite hockey player is Kaprisov
                        print("KIRILL THE THRILL" * 10)

                    else:
                        # The next three lines of code calculate the players average minutes on the ice per game
                        print("The next value is usually from 100 to 1000")
                        Icetime = int(input("Please enter the player's Icetime in minutes: "))
                        print("The next value is usually from 30 to 50")
                        Games_Played = int(input("Please enter the player's Games Played: "))
                        Icetime_Per_Game = Icetime / Games_Played

                        # On FanDuel you gain points for shots, blocked shots, assists, and goals
                        # The next three lines of code calculate the players average shots per game
                        print("The next value is usually from 50 to 200")
                        Shots_On_Goal = float(input("Please enter the player's Shots on Goal: "))
                        Shots_Per_Minute = Shots_On_Goal / Icetime
                        Shots_Per_Game = Shots_Per_Minute * Icetime_Per_Game

                        # The next three lines of code calculate the amount of shots the opponents may block per game
                        print("The next value is usually from 300 to 600")
                        Shots_Blocked_Team = float(input("Please enter the opponent team's shots blocked: "))
                        print("The next value is usually from 2000 to 3000")
                        Teams_Icetime = float(input("Please enter the opponent team's Icetime: "))
                        Shots_Blocked_Team_Per_Minute = Shots_Blocked_Team / Teams_Icetime
                        Defense_On_Player_Shots = Shots_Blocked_Team_Per_Minute * Icetime_Per_Game
                        # Players average shots minus opponets average blocked shots
                        Shots_Expected = Shots_Per_Game - Defense_On_Player_Shots
                        # On FanDuel, each shot is worth 1.6 points
                        Points_From_Shots = 1.6 * Shots_Expected

                        # The next three lines of code calculate the players average blocked shots per game
                        print("The next value is usually from 10 to 100")
                        Shots_Blocked = float(input("Please enter the player's Shots Blocked: "))
                        Shot_Blocks_Per_Minute = Shots_Blocked / Icetime
                        Shot_Blocks_Per_Game = Shot_Blocks_Per_Minute * Icetime_Per_Game
                        # On FanDuel, each blocked shot is worth 1.6 points
                        Points_From_Blocks = 1.6 * Shot_Blocks_Per_Game

                        # The next three lines of code calculate the players average assists per game
                        print("The next value is usually from 0 to 50")
                        Assists = float(input("Please enter the player's assists: "))
                        Assists_Per_Minute = Assists / Icetime
                        Assists_Per_Game = Assists_Per_Minute * Icetime_Per_Game
                        # On FanDuel, each assist is worth 8 points
                        Points_From_Assists = 8 * Assists_Per_Game

                        # The next three lines of code calculate the players average goals per game
                        print("The next value is usually from 0 to 50")
                        Goals = float(input("Please enter the player's goals: "))
                        Goals_Per_Minute = Goals / Icetime
                        Goals_Per_Game = Goals_Per_Minute * Icetime_Per_Game

                        # The next three lines of code calculate the opponets average goals defended per game
                        print("The next value is usually from -50 to 50")
                        Goals_Against_Below_Expected = float(
                            input("Please enter the player's opponents Goals Against Above Expected: "))
                        Goals_Defended_Per_Minute = Goals_Against_Below_Expected / Teams_Icetime
                        Defense_On_Player_Goals = Goals_Defended_Per_Minute * Icetime_Per_Game

                        # Players average goals minus opponents average goals defended
                        Goals_Expected = Goals_Per_Game + Defense_On_Player_Goals
                        # On FanDuel, each goal is 12 points
                        Points_From_Goals = 12 * Goals_Expected

                        # Adding up all expected points
                        Total_Points = Points_From_Shots + Points_From_Blocks + Points_From_Assists + Points_From_Goals
                        print("The player's expected fantasy points is ", format(Total_Points, "0.2f"), sep="")
                        print("The next value is usually from 3000 to 10500")
                        Cost = float(input("Please enter the cost of the player on FanDuel: "))

                        # This is how FanDuel determines the value of a player after a game has been completed
                        Value = (Total_Points / Cost) * 1000
                        # Preparing for string addition
                        Cost_String = str(format(Cost, "0.0f"))
                        Value_String = str(format(Value, "0.2f"))

                        if (Value >= 1.5):
                            print(Player_Name + " is worth their price of $" + Cost_String + " as they have an estimated value of " + Value_String)
                        else:
                            print(Player_Name + " is not worth their price of $" + Cost_String + " as they have an estimated value of " + Value_String)

                        print("If you would like to add this player to your line up, type YES. If not, type anything else")
                        Selection = input()

                        if Selection == "YES":
                            Center = Center - 1
                            Line_Up.append(Player_Name)
                            Total_Expected = Total_Expected + Total_Points
                            Total_Players += 1
                            Line_Up_Cost = Line_Up_Cost + Cost
                            if Total_Players < 9:
                                Average_Remaining = (Total_Cost - Line_Up_Cost) / (Number_Of_Players - Total_Players)
                                Average_String = str(format(Average_Remaining, "0.2f"))
                                print("This player was added to your line up and you have " + Average_String + " left for each remaining player.")
                            else:
                                print("You have completed your line up!")
                        else:
                            print("The player was not added.")
                else:
                    print("You already have too many players in this category, please pick a different player type.")

            elif Position == "Winger":
                if Winger != 0:
                    print("Please utilize moneypuck.com/stats.htm to enter requested data")
                    print("If you are not using moneypuck.com, enter values within the range printed before the input.")
                    Player_Name = input("Please enter the Player's name: ")

                    if (Player_Name == "Kirill Kaprisov"):
                        # This is to show string multiplication but also my favorite hockey player is Kaprisov
                        print("KIRILL THE THRILL" * 10)

                    else:
                        # The next three lines of code calculate the players average minutes on the ice per game
                        print("The next value is usually from 100 to 1000")
                        Icetime = int(input("Please enter the player's Icetime in minutes: "))
                        print("The next value is usually from 30 to 50")
                        Games_Played = int(input("Please enter the player's Games Played: "))
                        Icetime_Per_Game = Icetime / Games_Played

                        # On FanDuel you gain points for shots, blocked shots, assists, and goals
                        # The next three lines of code calculate the players average shots per game
                        print("The next value is usually from 50 to 200")
                        Shots_On_Goal = float(input("Please enter the player's Shots on Goal: "))
                        Shots_Per_Minute = Shots_On_Goal / Icetime
                        Shots_Per_Game = Shots_Per_Minute * Icetime_Per_Game

                        # The next three lines of code calculate the amount of shots the opponents may block per game
                        print("The next value is usually from 300 to 600")
                        Shots_Blocked_Team = float(input("Please enter the opponent team's shots blocked: "))
                        print("The next value is usually from 2000 to 3000")
                        Teams_Icetime = float(input("Please enter the opponent team's Icetime: "))
                        Shots_Blocked_Team_Per_Minute = Shots_Blocked_Team / Teams_Icetime
                        Defense_On_Player_Shots = Shots_Blocked_Team_Per_Minute * Icetime_Per_Game
                        # Players average shots minus opponets average blocked shots
                        Shots_Expected = Shots_Per_Game - Defense_On_Player_Shots
                        # On FanDuel, each shot is worth 1.6 points
                        Points_From_Shots = 1.6 * Shots_Expected

                        # The next three lines of code calculate the players average blocked shots per game
                        print("The next value is usually from 10 to 100")
                        Shots_Blocked = float(input("Please enter the player's Shots Blocked: "))
                        Shot_Blocks_Per_Minute = Shots_Blocked / Icetime
                        Shot_Blocks_Per_Game = Shot_Blocks_Per_Minute * Icetime_Per_Game
                        # On FanDuel, each blocked shot is worth 1.6 points
                        Points_From_Blocks = 1.6 * Shot_Blocks_Per_Game

                        # The next three lines of code calculate the players average assists per game
                        print("The next value is usually from 0 to 50")
                        Assists = float(input("Please enter the player's assists: "))
                        Assists_Per_Minute = Assists / Icetime
                        Assists_Per_Game = Assists_Per_Minute * Icetime_Per_Game
                        # On FanDuel, each assist is worth 8 points
                        Points_From_Assists = 8 * Assists_Per_Game

                        # The next three lines of code calculate the players average goals per game
                        print("The next value is usually from 0 to 50")
                        Goals = float(input("Please enter the player's goals: "))
                        Goals_Per_Minute = Goals / Icetime
                        Goals_Per_Game = Goals_Per_Minute * Icetime_Per_Game

                        # The next three lines of code calculate the opponets average goals defended per game
                        print("The next value is usually from -50 to 50")
                        Goals_Against_Below_Expected = float(
                            input("Please enter the player's opponents Goals Against Above Expected: "))
                        Goals_Defended_Per_Minute = Goals_Against_Below_Expected / Teams_Icetime
                        Defense_On_Player_Goals = Goals_Defended_Per_Minute * Icetime_Per_Game

                        # Players average goals minus opponents average goals defended
                        Goals_Expected = Goals_Per_Game + Defense_On_Player_Goals
                        # On FanDuel, each goal is 12 points
                        Points_From_Goals = 12 * Goals_Expected

                        # Adding up all expected points
                        Total_Points = Points_From_Shots + Points_From_Blocks + Points_From_Assists + Points_From_Goals
                        print("The player's expected fantasy points is ", format(Total_Points, "0.2f"), sep="")
                        print("The next value is usually from 3000 to 10500")
                        Cost = float(input("Please enter the cost of the player on FanDuel: "))

                        # This is how FanDuel determines the value of a player after a game has been completed
                        Value = (Total_Points / Cost) * 1000
                        # Preparing for string addition
                        Cost_String = str(format(Cost, "0.0f"))
                        Value_String = str(format(Value, "0.2f"))

                        if (Value >= 1.5):
                            print(Player_Name + " is worth their price of $" + Cost_String + " as they have an estimated value of " + Value_String)
                        else:
                            print(Player_Name + " is not worth their price of $" + Cost_String + " as they have an estimated value of " + Value_String)

                        print("If you would like to add this player to your line up, type YES. If not, type anything else")
                        Selection = input()

                        if Selection == "YES":
                            Winger = Winger - 1
                            Line_Up.append(Player_Name)
                            Total_Expected = Total_Expected + Total_Points
                            Total_Players += 1
                            Line_Up_Cost = Line_Up_Cost + Cost
                            if Total_Players < 9:
                                Average_Remaining = (Total_Cost - Line_Up_Cost) / (Number_Of_Players - Total_Players)
                                Average_String = str(format(Average_Remaining, "0.2f"))
                                print("This player was added to your line up and you have " + Average_String + " left for each remaining player.")
                            else:
                                print("You have completed your line up!")
                        else:
                            print("The player was not added.")
                else:
                    print("You already have too many players in this category, please pick a different player type.")

            elif Position == "Defense":
                if Defense != 0:
                    print("Please utilize moneypuck.com/stats.htm to enter requested data")
                    print("If you are not using moneypuck.com, enter values within the range printed before the input.")
                    Player_Name = input("Please enter the Player's name: ")

                    if (Player_Name == "Kirill Kaprisov"):
                        # This is to show string multiplication but also my favorite hockey player is Kaprisov
                        print("KIRILL THE THRILL" * 10)

                    else:
                        # The next three lines of code calculate the players average minutes on the ice per game
                        print("The next value is usually from 100 to 1000")
                        Icetime = int(input("Please enter the player's Icetime in minutes: "))
                        print("The next value is usually from 30 to 50")
                        Games_Played = int(input("Please enter the player's Games Played: "))
                        Icetime_Per_Game = Icetime / Games_Played

                        # On FanDuel you gain points for shots, blocked shots, assists, and goals
                        # The next three lines of code calculate the players average shots per game
                        print("The next value is usually from 50 to 200")
                        Shots_On_Goal = float(input("Please enter the player's Shots on Goal: "))
                        Shots_Per_Minute = Shots_On_Goal / Icetime
                        Shots_Per_Game = Shots_Per_Minute * Icetime_Per_Game

                        # The next three lines of code calculate the amount of shots the opponents may block per game
                        print("The next value is usually from 300 to 600")
                        Shots_Blocked_Team = float(input("Please enter the opponent team's shots blocked: "))
                        print("The next value is usually from 2000 to 3000")
                        Teams_Icetime = float(input("Please enter the opponent team's Icetime: "))
                        Shots_Blocked_Team_Per_Minute = Shots_Blocked_Team / Teams_Icetime
                        Defense_On_Player_Shots = Shots_Blocked_Team_Per_Minute * Icetime_Per_Game
                        # Players average shots minus opponets average blocked shots
                        Shots_Expected = Shots_Per_Game - Defense_On_Player_Shots
                        # On FanDuel, each shot is worth 1.6 points
                        Points_From_Shots = 1.6 * Shots_Expected

                        # The next three lines of code calculate the players average blocked shots per game
                        print("The next value is usually from 10 to 100")
                        Shots_Blocked = float(input("Please enter the player's Shots Blocked: "))
                        Shot_Blocks_Per_Minute = Shots_Blocked / Icetime
                        Shot_Blocks_Per_Game = Shot_Blocks_Per_Minute * Icetime_Per_Game
                        # On FanDuel, each blocked shot is worth 1.6 points
                        Points_From_Blocks = 1.6 * Shot_Blocks_Per_Game

                        # The next three lines of code calculate the players average assists per game
                        print("The next value is usually from 0 to 50")
                        Assists = float(input("Please enter the player's assists: "))
                        Assists_Per_Minute = Assists / Icetime
                        Assists_Per_Game = Assists_Per_Minute * Icetime_Per_Game
                        # On FanDuel, each assist is worth 8 points
                        Points_From_Assists = 8 * Assists_Per_Game

                        # The next three lines of code calculate the players average goals per game
                        print("The next value is usually from 0 to 50")
                        Goals = float(input("Please enter the player's goals: "))
                        Goals_Per_Minute = Goals / Icetime
                        Goals_Per_Game = Goals_Per_Minute * Icetime_Per_Game

                        # The next three lines of code calculate the opponets average goals defended per game
                        print("The next value is usually from -50 to 50")
                        Goals_Against_Below_Expected = float(
                            input("Please enter the player's opponents Goals Against Above Expected: "))
                        Goals_Defended_Per_Minute = Goals_Against_Below_Expected / Teams_Icetime
                        Defense_On_Player_Goals = Goals_Defended_Per_Minute * Icetime_Per_Game

                        # Players average goals minus opponents average goals defended
                        Goals_Expected = Goals_Per_Game + Defense_On_Player_Goals
                        # On FanDuel, each goal is 12 points
                        Points_From_Goals = 12 * Goals_Expected

                        # Adding up all expected points
                        Total_Points = Points_From_Shots + Points_From_Blocks + Points_From_Assists + Points_From_Goals
                        print("The player's expected fantasy points is ", format(Total_Points, "0.2f"), sep="")
                        print("The next value is usually from 3000 to 10500")
                        Cost = float(input("Please enter the cost of the player on FanDuel: "))

                        # This is how FanDuel determines the value of a player after a game has been completed
                        Value = (Total_Points / Cost) * 1000
                        # Preparing for string addition
                        Cost_String = str(format(Cost, "0.0f"))
                        Value_String = str(format(Value, "0.2f"))

                        if (Value >= 1.5):
                            print(Player_Name + " is worth their price of $" + Cost_String + " as they have an estimated value of " + Value_String)
                        else:
                            print(Player_Name + " is not worth their price of $" + Cost_String + " as they have an estimated value of " + Value_String)

                        print("If you would like to add this player to your line up, type YES. If not, type anything else")
                        Selection = input()

                        if Selection == "YES":
                            Defense = Defense - 1
                            Line_Up.append(Player_Name)
                            Total_Expected = Total_Expected + Total_Points
                            Total_Players += 1
                            Line_Up_Cost = Line_Up_Cost + Cost
                            if Total_Players < 9:
                                Average_Remaining = (Total_Cost - Line_Up_Cost) / (Number_Of_Players - Total_Players)
                                Average_String = str(format(Average_Remaining, "0.2f"))
                                print("This player was added to your line up and you have " + Average_String + " left for each remaining player.")
                            else:
                                print("You have completed your line up!")
                        else:
                            print("The player was not added.")
                else:
                    print("You already have too many players in this category, please pick a different player type.")

            elif Position == "Utility":
                if (Center != 0) or (Winger != 0) or (Defense != 0) or (Goalie != 0):
                    print("I would suggest filling out other roles before picking Utility Players")

                elif Utility != 0:
                    print("Please utilize moneypuck.com/stats.htm to enter requested data")
                    print("If you are not using moneypuck.com, enter values within the range printed before the input.")
                    Player_Name = input("Please enter the Player's name: ")

                    if (Player_Name == "Kirill Kaprisov"):
                        # This is to show string multiplication but also my favorite hockey player is Kaprisov
                        print("KIRILL THE THRILL" * 10)

                    else:
                        # The next three lines of code calculate the players average minutes on the ice per game
                        print("The next value is usually from 100 to 1000")
                        Icetime = int(input("Please enter the player's Icetime in minutes: "))
                        print("The next value is usually from 30 to 50")
                        Games_Played = int(input("Please enter the player's Games Played: "))
                        Icetime_Per_Game = Icetime / Games_Played

                        # On FanDuel you gain points for shots, blocked shots, assists, and goals
                        # The next three lines of code calculate the players average shots per game
                        print("The next value is usually from 50 to 200")
                        Shots_On_Goal = float(input("Please enter the player's Shots on Goal: "))
                        Shots_Per_Minute = Shots_On_Goal / Icetime
                        Shots_Per_Game = Shots_Per_Minute * Icetime_Per_Game

                        # The next three lines of code calculate the amount of shots the opponents may block per game
                        print("The next value is usually from 300 to 600")
                        Shots_Blocked_Team = float(input("Please enter the opponent team's shots blocked: "))
                        print("The next value is usually from 2000 to 3000")
                        Teams_Icetime = float(input("Please enter the opponent team's Icetime: "))
                        Shots_Blocked_Team_Per_Minute = Shots_Blocked_Team / Teams_Icetime
                        Defense_On_Player_Shots = Shots_Blocked_Team_Per_Minute * Icetime_Per_Game
                        # Players average shots minus opponets average blocked shots
                        Shots_Expected = Shots_Per_Game - Defense_On_Player_Shots
                        # On FanDuel, each shot is worth 1.6 points
                        Points_From_Shots = 1.6 * Shots_Expected

                        # The next three lines of code calculate the players average blocked shots per game
                        print("The next value is usually from 10 to 100")
                        Shots_Blocked = float(input("Please enter the player's Shots Blocked: "))
                        Shot_Blocks_Per_Minute = Shots_Blocked / Icetime
                        Shot_Blocks_Per_Game = Shot_Blocks_Per_Minute * Icetime_Per_Game
                        # On FanDuel, each blocked shot is worth 1.6 points
                        Points_From_Blocks = 1.6 * Shot_Blocks_Per_Game

                        # The next three lines of code calculate the players average assists per game
                        print("The next value is usually from 0 to 50")
                        Assists = float(input("Please enter the player's assists: "))
                        Assists_Per_Minute = Assists / Icetime
                        Assists_Per_Game = Assists_Per_Minute * Icetime_Per_Game
                        # On FanDuel, each assist is worth 8 points
                        Points_From_Assists = 8 * Assists_Per_Game

                        # The next three lines of code calculate the players average goals per game
                        print("The next value is usually from 0 to 50")
                        Goals = float(input("Please enter the player's goals: "))
                        Goals_Per_Minute = Goals / Icetime
                        Goals_Per_Game = Goals_Per_Minute * Icetime_Per_Game

                        # The next three lines of code calculate the opponets average goals defended per game
                        print("The next value is usually from -50 to 50")
                        Goals_Against_Below_Expected = float(
                            input("Please enter the player's opponents Goals Against Above Expected: "))
                        Goals_Defended_Per_Minute = Goals_Against_Below_Expected / Teams_Icetime
                        Defense_On_Player_Goals = Goals_Defended_Per_Minute * Icetime_Per_Game

                        # Players average goals minus opponents average goals defended
                        Goals_Expected = Goals_Per_Game + Defense_On_Player_Goals
                        # On FanDuel, each goal is 12 points
                        Points_From_Goals = 12 * Goals_Expected

                        # Adding up all expected points
                        Total_Points = Points_From_Shots + Points_From_Blocks + Points_From_Assists + Points_From_Goals
                        print("The player's expected fantasy points is ", format(Total_Points, "0.2f"), sep="")
                        print("The next value is usually from 3000 to 10500")
                        Cost = float(input("Please enter the cost of the player on FanDuel: "))

                        # This is how FanDuel determines the value of a player after a game has been completed
                        Value = (Total_Points / Cost) * 1000
                        # Preparing for string addition
                        Cost_String = str(format(Cost, "0.0f"))
                        Value_String = str(format(Value, "0.2f"))

                        if (Value >= 1.5):
                            print(Player_Name + " is worth their price of $" + Cost_String + " as they have an estimated value of " + Value_String)
                        else:
                            print(Player_Name + " is not worth their price of $" + Cost_String + " as they have an estimated value of " + Value_String)

                        print("If you would like to add this player to your line up, type YES. If not, type anything else")
                        Selection = input()

                        if Selection == "YES":
                            Utility = Utility - 1
                            Line_Up.append(Player_Name)
                            Total_Expected = Total_Expected + Total_Points
                            Total_Players += 1
                            Line_Up_Cost = Line_Up_Cost + Cost
                            if Total_Players < 9:
                                Average_Remaining = (Total_Cost - Line_Up_Cost) / (Number_Of_Players - Total_Players)
                                Average_String = str(format(Average_Remaining, "0.2f"))
                                print("This player was added to your line up and you have " + Average_String + " left for each remaining player.")
                            else:
                                print("You have completed your line up!")
                        else:
                            print("The player was not added.")
                else:
                    print("You already have too many players in this category, please pick a different player type.")

            elif Position == "Goalie":
                if Goalie != 0:
                    print("Please utilize moneypuck.com/stats.htm to enter requested data")
                    print("If you are not using moneypuck.com, enter values within the range printed before the input.")
                    Player_Name = input("Please enter the Goalie's name: ")

                    if (Player_Name == "Kirill Kaprisov"):
                        # This is to show string multiplication but also my favorite hockey player is Kaprisov
                        print("KIRILL THE THRILL" * 10)

                    else:
                        # The next four lines of code calculate the goalie's average goails against for the game
                        print("The next value is usually from 1.00 to 4.00")
                        Goals_Against_Average = float(input("Please enter the goalie's goals against average: "))
                        print("The next value is usually from 100 to 200")
                        Opponents_Goals_For = float(input("Please enter the opponent's total goals for: "))
                        print("The next value is usually from 40 to 50")
                        Opponents_Games_Played = float(input("Please enter the number of games the opponent has played: "))
                        Opponents_Goals_Per_Game = Opponents_Goals_For / Opponents_Games_Played

                        # Taking the average of goalie's goals against and opponents goals for
                        Expected_Goals_Against = (Goals_Against_Average + Opponents_Goals_Per_Game) / 2
                        # Each goal against is minus 4 points so we will subtract this value later
                        Points_From_Goals_Against = 4 * Expected_Goals_Against

                        # The next three lines of code calculate the goalie's saves per game
                        print("The next value is usually from 1000 to 2000")
                        Opponents_Shots = float(input("Please enter the opponent's total shots: "))
                        Opponents_Shots_Per_Game = Opponents_Shots / Opponents_Games_Played
                        # Opponents shots minus goals scored equals goalie's saves
                        Goalies_Expected_Saves = Opponents_Shots_Per_Game - Expected_Goals_Against
                        # On FanDuel, each save is 0.8 points
                        Points_From_Saves = 0.8 * Goalies_Expected_Saves

                        # Teams Win Probability
                        # Since this really has nothing to do with the goalie but gives the goalie points, I am just using the win probability
                        print("The next value is usually from 0.000 to 1.000")
                        Teams_Win_Probability = float(input("Please enter the teams win probability in decimal form: "))
                        # On FanDuel, a win is 12 points
                        Points_From_Win = 12 * Teams_Win_Probability

                        # Shutout Probability (Goalie lets in no goals)
                        print("The next value is usually from 0.700 to 1.000")
                        Save_Percentage = float(input("Please enter the goalie's save percentage in decimal form: "))
                        # A goalie can be very good on average, usually shown by save percentage rather than goals against average
                        # Multiplied by opponents shots to get estimated goals against
                        Possible_Goals_Against = Opponents_Goals_Per_Game * Save_Percentage
                        # An estimate on the probability of saving those expected goals against
                        Shutout_Probability = (1 / Possible_Goals_Against) ** 2
                        # On FanDuel, a shutout is 8 points
                        Points_From_Shutout = 8 * Shutout_Probability

                        # Adding up all expected points and subtracting the poitns from goals against
                        Total_Points = Points_From_Saves + Points_From_Win + Points_From_Shutout - Points_From_Goals_Against
                        print("The goalie's expected fantasy points is ", format(Total_Points, "0.2f"), sep="")
                        print("The next value is usually from 3500 to 10500")
                        Cost = float(input("Please enter the cost of the goalie on FanDuel: "))

                        # This is how FanDuel determines the value of a player after a game has been completed
                        Value = (Total_Points / Cost) * 1000
                        # Preparing for string addition
                        Cost_String = str(format(Cost, "0.0f"))
                        Value_String = str(format(Value, "0.2f"))
                        if (Value >= 1.5):
                            print(Player_Name + " is worth their price of $" + Cost_String + " as they have an estimated value of " + Value_String)
                        else:
                            print(Player_Name + " is not worth their price of $" + Cost_String + " as they have an estimated value of " + Value_String)

                        print("If you would like to add this player to your line up, type YES. If not, type anything else")
                        Selection = input()

                        if Selection == "YES":
                            Goalie = Goalie - 1
                            Line_Up.append(Player_Name)
                            Total_Expected = Total_Expected + Total_Points
                            Total_Players += 1
                            Line_Up_Cost = Line_Up_Cost + Cost
                            if Total_Players < 9:
                                Average_Remaining = (Total_Cost - Line_Up_Cost) / (Number_Of_Players - Total_Players)
                                Average_String = str(format(Average_Remaining, "0.2f"))
                                print("This player was added to your line up and you have " + Average_String + " left for each remaining player.")
                            else:
                                print("You have completed your line up!")
                        else:
                            print("The player was not added.")
                else:
                    print("You already have too many players in this category, please pick a different player type.")
            else:
                print("Please type one of the options below.")
        else:
            print("You have gone over budget, you have to restart and pick some cheaper players!")
            quit(main)
    print("Your line up is:")
    for x in range(len(Line_Up)):
        print(Line_Up[x])

    print("Your expected points are", Total_Expected)
    if not(Total_Cost == Line_Up_Cost):
        print("You have money left over so it is possible to make a better line up.")

main()
print("Good Luck!")

#I didn't have anywhere to use AND so here it is
Favorite_Team = input("Who is your favorite hockey team?")
Favorite_Player = input("Who is your favoirte player?")
if Favorite_Team == "Minnesota Wild" and Favorite_Player == "Kirill Kaprisov":
    print("Correct.")
elif Favorite_Team == "Minnesota Wild" or Favorite_Player == "Kirill Kaprisov":
    print("Almost.")
else:
    print("Wrong.")

