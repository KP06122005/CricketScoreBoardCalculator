
print("Welcome to KP's Advanced CricCalcItUp Cricket Calculator")
print("-----------------------------------------------------------------------------------")




def PlayerInput(Num):  # Player Input Function
    ListOfPlayers = []
    for i in range(1, Num + 1):
        while True:
            print("Player Number: " + str(i))
            PlayerName = input("Enter player name: ")
            if PlayerName:
                ListOfPlayers.append(PlayerName)
                break
            else:
                print("Enter Proper Input")
    return ListOfPlayers

def Swap(A, B):
    return B, A

def BowlerChange(list):
    i = 0
    while i == 0:
        Name = str(input("Enter the Name of the Bowler: "))
        if Name in list:
            print("Selected Bowler: " + Name)
            i += 1
            return Name
        else:
            print("Enter Proper Input")

# Input for Name of the Participants
def Check(Score1,Score2):
    if Score1 > Score2:
        return 1
    elif Score1 < Score2:
        return 2
    else:
        return 0
while True:
    TeamA = input("Enter the Name of Team A: ")
    if TeamA:
        break
    else:
        print("Enter Proper Input")

while True:
    TeamB = input("Enter the Name of Team B: ")
    if TeamB:
        break
    else:
        print("Enter Proper Input")
print("-----------------------------------------------------------------------------------")


# Input for Toss
while True:
    Toss = input("Who won the Toss? ")
    if Toss == TeamA or Toss == TeamB:
        break
    else:
        print("Enter Proper Input")

while True:
    Decision_Toss = input("Bat/Bowl: ").strip().capitalize()
    if Decision_Toss in ["Bat", "Bowl"]:
        break
    else:
        print("Enter Proper Input")
print("-----------------------------------------------------------------------------------")

# Number of Players per Team
while True:
    try:
        NumOfPlayers = int(input("Number of Players per Team: "))
        if NumOfPlayers > 0:
            break
        else:
            print("Enter a positive number")
    except ValueError:
        print("Enter a valid number")
print("-----------------------------------------------------------------------------------")


# Player List
print("Members of Team " + TeamA)
ListOfA = PlayerInput(NumOfPlayers)
print("-----------------------------------------------------------------------------------")

print("Members of Team " + TeamB)
ListOfB = PlayerInput(NumOfPlayers)
print("-----------------------------------------------------------------------------------")


# Game Rules
while True:
    try:
        NumOfOvers = int(input("Enter the Number of Overs: "))
        if NumOfOvers > 0:
            break
        else:
            print("Enter a positive number")
    except ValueError:
        print("Enter a valid number")
print("-----------------------------------------------------------------------------------")

# Batsman data
ListOfScoresA = [0] * NumOfPlayers
ListOfBallsPlayedA = [0] * NumOfPlayers
ListOf4sA = [0] * NumOfPlayers
ListOf6sA = [0] * NumOfPlayers
MOD_A = ["Not Out"] * NumOfPlayers

# Bowler data
ListOfOversA = [0] * NumOfPlayers
ListOfRunsGivenA = [0] * NumOfPlayers
ListOfWicksA = [0] * NumOfPlayers
ListOfMaidensA = [0] * NumOfPlayers

# Batsman data
ListOfScoresB = [0] * NumOfPlayers
ListOfBallsPlayedB = [0] * NumOfPlayers
ListOf4sB = [0] * NumOfPlayers
ListOf6sB = [0] * NumOfPlayers
MOD_B = ["Not Out"] * NumOfPlayers

# Bowler data
ListOfOversB = [0] * NumOfPlayers
ListOfRunsGivenB = [0] * NumOfPlayers
ListOfWicksB = [0] * NumOfPlayers
ListOfMaidensB = [0] * NumOfPlayers

# Game Data
ScoreA = 0
ScoreB = 0
WicksA = 0
WicksB = 0
WicksRemA = (NumOfPlayers - 1) - WicksA
WicksRemB = (NumOfPlayers - 1) - WicksB
BallCounter = NumOfOvers * 6
OverCounter = 0

print("Match Starts")
# Team A is Batting
# Team B is Bowling


if (Toss == TeamA and Decision_Toss == "Bat") or (Toss == TeamB and Decision_Toss == "Bowl"):
    Striker = 0
    NonStriker = 1
    print(str(TeamA) + " is Batting and " + str(TeamB) + " is Bowling")
    print("First Inning Starts")
    print("-----------------------------------------------------------------------------------")

    while OverCounter != NumOfOvers and WicksA < NumOfPlayers - 1:
        Bowler = BowlerChange(ListOfB)
        balls_in_over = 0  # Track the number of balls bowled in the current over
        while balls_in_over < 6:
            print(Bowler + " to " + ListOfA[Striker])
            Event = input("Enter the Event: ").strip().lower()
            if Event in ["4", "6", "2", "1", "3", "extras", "wick","5","0"]:
                if Event == "4":
                    ScoreA += 4
                    ListOfScoresA[Striker] += 4
                    ListOfBallsPlayedA[Striker] += 1
                    ListOf4sA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 4
                elif Event == "0":
                    ListOfBallsPlayedA[Striker] += 1
                elif Event == "6":
                    ScoreA += 6
                    ListOfScoresA[Striker] += 6
                    ListOfBallsPlayedA[Striker] += 1
                    ListOf6sA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 6
                elif Event == "2":
                    ScoreA += 2
                    ListOfScoresA[Striker] += 2
                    ListOfBallsPlayedA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 2
                elif Event == "extras":
                    EventInExtras = input("wide?/nb? : ")
                    ScoreA += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 1
                    RunsInExtras = int(input("Runs in Wide byes or no ball byes ? : "))
                    ScoreA += RunsInExtras
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += RunsInExtras
                    if EventInExtras == "nb":
                        RunsInExtrasBat = int(input("Runs off Bat in extras ? : "))
                        ScoreA += RunsInExtrasBat
                        ListOfScoresA[Striker] += RunsInExtrasBat
                        ListOfRunsGivenB[ListOfB.index(Bowler)] += RunsInExtrasBat
                    # Do not count this as a ball bowled
                    continue
                elif Event == "lgb":
                    RunsInLgb = int(input("Runs Scored in Leg Byes : "))
                    ScoreA += RunsInLgb
                    ListOfBallsPlayedA[Striker] += 1
                elif Event == "1":
                    ScoreA += 1
                    ListOfScoresA[Striker] += 1
                    ListOfBallsPlayedA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 1
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "3":
                    ScoreA += 3
                    ListOfScoresA[Striker] += 3
                    ListOfBallsPlayedA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 3
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "5":
                    ScoreA += 5
                    ListOfScoresA[Striker] += 5
                    ListOfBallsPlayedA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 5
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "wick":
                    while True:
                        PlayerOut = input("Who is Out? ")
                        if PlayerOut in ListOfA:
                            break
                        else:
                            print("Enter Proper Input")
                    IndexOfOut = ListOfA.index(PlayerOut)
                    Dismissal = input("Mode of Dismissal? ")
                    MOD_A[Striker] = Dismissal
                    ListOfBallsPlayedA[Striker] += 1
                    ListOfWicksB[ListOfB.index(Bowler)] += 1
                    WicksA += 1
                    if WicksA < NumOfPlayers - 1:
                        Striker = WicksA + 1
                    else:
                        print("All out!")
                        OverCounter = NumOfOvers
                        break
                balls_in_over += 1
            else:
                print("Enter Proper Input")

        if ListOfRunsGivenB[ListOfB.index(Bowler)] == 0:
            ListOfMaidensB[ListOfB.index(Bowler)] += 1

        OverCounter += 1
        ListOfOversB[ListOfB.index(Bowler)] += 1

        # Swap at the end of the over only if the last run was not odd
        if Event not in ["1", "3","5"]:
            Striker, NonStriker = Swap(Striker, NonStriker)
    print("First Innings Ends")
    print(TeamA + " : " +  str(ScoreA) + "/" + str(WicksA))
    print("-----------------------------------------------------------------------------------")

    print(str(TeamB) + " is Batting and " + str(TeamA) + " is Bowling")
    print("Second Inning Starts")
    OverCounter = 0
    Striker = 0
    NonStriker = 1
    while OverCounter != NumOfOvers and WicksB < NumOfPlayers - 1 :
        Bowler = BowlerChange(ListOfA)
        balls_in_over = 0  # Track the number of balls bowled in the current over
        while balls_in_over < 6 :
            print(Bowler + " to " + ListOfB[Striker])
            Event = input("Enter the Event: ").strip().lower()
            if Event in ["4", "6", "2", "1", "3", "extras", "wick", "5","0"]:
                if Event == "4":
                    ScoreB += 4
                    ListOfScoresB[Striker] += 4
                    ListOfBallsPlayedB[Striker] += 1
                    ListOf4sB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 4
                elif Event == "0":
                    ListOfBallsPlayedB[Striker] += 1
                elif Event == "6":
                    ScoreB += 6
                    ListOfScoresB[Striker] += 6
                    ListOfBallsPlayedB[Striker] += 1
                    ListOf6sB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 6
                elif Event == "2":
                    ScoreB += 2
                    ListOfScoresB[Striker] += 2
                    ListOfBallsPlayedB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 2
                elif Event == "extras":
                    EventInExtras = input("wide?/nb? : ")
                    ScoreB += 1
                    ListOfRunsGivenA[ListOfB.index(Bowler)] += 1
                    RunsInExtras = int(input("Runs in Wide byes or no ball byes ? : "))
                    ScoreB += RunsInExtras
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += RunsInExtras
                    if EventInExtras == "nb":
                        RunsInExtrasBat = int(input("Runs off Bat in extras ? : "))
                        ScoreB += RunsInExtrasBat
                        ListOfScoresB[Striker] += RunsInExtrasBat
                        ListOfRunsGivenA[ListOfA.index(Bowler)] += RunsInExtrasBat
                    # Do not count this as a ball bowled
                    continue
                elif Event == "lgb":
                    RunsInLgb = int(input("Runs Scored in Leg Byes : "))
                    ScoreB += RunsInLgb
                    ListOfBallsPlayedB[Striker] += 1
                elif Event == "1":
                    ScoreB += 1
                    ListOfScoresB[Striker] += 1
                    ListOfBallsPlayedB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 1
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "3":
                    ScoreB += 3
                    ListOfScoresB[Striker] += 3
                    ListOfBallsPlayedB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 3
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "5":
                    ScoreB += 5
                    ListOfScoresB[Striker] += 5
                    ListOfBallsPlayedB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 5
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "wick":
                    while True:
                        PlayerOut = input("Who is Out? ")
                        if PlayerOut in ListOfB:
                            break
                        else:
                            print("Enter Proper Input")
                    IndexOfOut = ListOfB.index(PlayerOut)
                    Dismissal = input("Mode of Dismissal? ")
                    MOD_B[Striker] = Dismissal
                    ListOfBallsPlayedB[Striker] += 1
                    ListOfWicksA[ListOfA.index(Bowler)] += 1
                    WicksB += 1
                    if WicksB < NumOfPlayers - 1:
                        Striker = WicksB + 1
                    else:
                        print("All out!")
                        OverCounter = NumOfOvers
                        break
                if Check(ScoreA, ScoreB) == 2:
                    break
                balls_in_over += 1
            else:
                print("Enter Proper Input")

        if ListOfRunsGivenA[ListOfA.index(Bowler)] == 0:
            ListOfMaidensA[ListOfA.index(Bowler)] += 1
        ListOfOversA[ListOfA.index(Bowler)] += 1
        if Check(ScoreA,ScoreB) == 2:
            break
        OverCounter += 1


        # Swap at the end of the over only if the last run was not odd
        if Event not in ["1", "3", "5"]:
            Striker, NonStriker = Swap(Striker, NonStriker)
    print(TeamB + " : " + str(ScoreB) + "/" + str(WicksB))
    Checker = Check(ScoreA,ScoreB)
    if Checker == 1:
        print(TeamA + " won by " + str(ScoreA - ScoreB) + " runs")
    elif Checker == 2:
        print(TeamB + " won by " + str(NumOfPlayers - 1 - WicksB) + " wickets")
    elif Checker == 0:
        print("Match is drawn")
    else:
        print("No Result")
    print("-----------------------------------------------------------------------------------")






else:
    Striker = 0
    NonStriker = 1
    print(TeamB + " is Batting and " + TeamA + " is Bowling")
    print("First Inning Starts")
    print("-----------------------------------------------------------------------------------")
    while OverCounter != NumOfOvers and WicksB < NumOfPlayers - 1:
        Bowler = BowlerChange(ListOfA)
        balls_in_over = 0  # Track the number of balls bowled in the current over
        while balls_in_over < 6:
            print(Bowler + " to " + ListOfB[Striker])
            Event = input("Enter the Event: ").strip().lower()
            if Event in ["4", "6", "2", "1", "3", "extras", "wick", "5","0"]:
                if Event == "4":
                    ScoreB += 4
                    ListOfScoresB[Striker] += 4
                    ListOfBallsPlayedB[Striker] += 1
                    ListOf4sB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 4
                elif Event == "0":
                    ListOfBallsPlayedB[Striker] += 1
                elif Event == "6":
                    ScoreB += 6
                    ListOfScoresB[Striker] += 6
                    ListOfBallsPlayedB[Striker] += 1
                    ListOf6sB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 6
                elif Event == "2":
                    ScoreB += 2
                    ListOfScoresB[Striker] += 2
                    ListOfBallsPlayedB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 2
                elif Event == "extras":
                    EventInExtras = input("wide?/nb? : ")
                    ScoreB += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 1
                    RunsInExtras = int(input("Runs in Wide byes or no ball byes ? : "))
                    ScoreB += RunsInExtras
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += RunsInExtras
                    if EventInExtras == "nb":
                        RunsInExtrasBat = int(input("Runs off Bat in extras ? : "))
                        ScoreB += RunsInExtrasBat
                        ListOfScoresB[Striker] += RunsInExtrasBat
                        ListOfRunsGivenA[ListOfA.index(Bowler)] += RunsInExtrasBat
                    # Do not count this as a ball bowled
                    continue
                elif Event == "lgb":
                    RunsInLgb = int(input("Runs Scored in Leg Byes : "))
                    ScoreB += RunsInLgb
                    ListOfBallsPlayedB[Striker] += 1
                elif Event == "1":
                    ScoreB += 1
                    ListOfScoresB[Striker] += 1
                    ListOfBallsPlayedB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 1
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "3":
                    ScoreB += 3
                    ListOfScoresB[Striker] += 3
                    ListOfBallsPlayedB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 3
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "5":
                    ScoreB += 5
                    ListOfScoresB[Striker] += 5
                    ListOfBallsPlayedB[Striker] += 1
                    ListOfRunsGivenA[ListOfA.index(Bowler)] += 5
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "wick":
                    while True:
                        PlayerOut = input("Who is Out? ")
                        if PlayerOut in ListOfB:
                            break
                        else:
                            print("Enter Proper Input")
                    IndexOfOut = ListOfB.index(PlayerOut)
                    Dismissal = input("Mode of Dismissal? ")
                    MOD_B[Striker] = Dismissal
                    ListOfBallsPlayedB[Striker] += 1
                    ListOfWicksA[ListOfA.index(Bowler)] += 1
                    WicksB += 1
                    if WicksB < NumOfPlayers - 1:
                        Striker = WicksB + 1
                    else:
                        print("All out!")
                        OverCounter = NumOfOvers
                        break
                balls_in_over += 1
            else:
                print("Enter Proper Input")

        if ListOfRunsGivenA[ListOfA.index(Bowler)] == 0:
            ListOfMaidensA[ListOfA.index(Bowler)] += 1

        OverCounter += 1
        ListOfOversA[ListOfA.index(Bowler)] += 1

        # Swap at the end of the over only if the last run was not odd
        if Event not in ["1", "3", "5"]:
            Striker, NonStriker = Swap(Striker, NonStriker)
    print("First Innings Ends")
    print(TeamB + " : " + str(ScoreB) + "/" + str(WicksB))
    print("-----------------------------------------------------------------------------------")

    print(str(TeamA) + " is Batting and " + str(TeamB) + " is Bowling")
    print("Second Inning Starts")


    OverCounter = 0
    Striker = 0
    NonStriker = 1
    while OverCounter != NumOfOvers and WicksA < NumOfPlayers - 1:
        Bowler = BowlerChange(ListOfB)
        balls_in_over = 0  # Track the number of balls bowled in the current over
        while balls_in_over < 6:
            print(Bowler + " to " + ListOfA[Striker])
            Event = input("Enter the Event: ").strip().lower()
            if Event in ["4", "6", "2", "1", "3", "extras", "wick", "5","0"]:
                if Event == "4":
                    ScoreA += 4
                    ListOfScoresA[Striker] += 4
                    ListOfBallsPlayedA[Striker] += 1
                    ListOf4sA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 4
                elif Event == "0":
                    ListOfBallsPlayedA[Striker] += 1
                elif Event == "6":
                    ScoreA += 6
                    ListOfScoresA[Striker] += 6
                    ListOfBallsPlayedA[Striker] += 1
                    ListOf6sA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 6
                elif Event == "2":
                    ScoreA += 2
                    ListOfScoresA[Striker] += 2
                    ListOfBallsPlayedA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 2
                elif Event == "extras":
                    EventInExtras = input("wide?/nb? : ")
                    ScoreA += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 1
                    RunsInExtras = int(input("Runs in Wide byes or no ball byes ? : "))
                    ScoreA += RunsInExtras
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += RunsInExtras
                    if EventInExtras == "nb":
                        RunsInExtrasBat = int(input("Runs off Bat in extras ? : "))
                        ScoreA += RunsInExtrasBat
                        ListOfScoresA[Striker] += RunsInExtrasBat
                        ListOfRunsGivenB[ListOfB.index(Bowler)] += RunsInExtrasBat
                    # Do not count this as a ball bowled
                    continue
                elif Event == "lgb":
                    RunsInLgb = int(input("Runs Scored in Leg Byes : "))
                    ScoreA += RunsInLgb
                    ListOfBallsPlayedA[Striker] += 1
                elif Event == "1":
                    ScoreA += 1
                    ListOfScoresA[Striker] += 1
                    ListOfBallsPlayedA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 1
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "3":
                    ScoreA += 3
                    ListOfScoresA[Striker] += 3
                    ListOfBallsPlayedA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 3
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "5":
                    ScoreA += 5
                    ListOfScoresA[Striker] += 5
                    ListOfBallsPlayedA[Striker] += 1
                    ListOfRunsGivenB[ListOfB.index(Bowler)] += 5
                    if (balls_in_over != 5):
                        Striker, NonStriker = Swap(Striker, NonStriker)
                elif Event == "wick":
                    while True:
                        PlayerOut = input("Who is Out? ")
                        if PlayerOut in ListOfA:
                            break
                        else:
                            print("Enter Proper Input")
                    IndexOfOut = ListOfA.index(PlayerOut)
                    Dismissal = input("Mode of Dismissal? ")
                    MOD_A[Striker] = Dismissal
                    ListOfBallsPlayedA[Striker] += 1
                    ListOfWicksB[ListOfB.index(Bowler)] += 1
                    WicksA += 1
                    if WicksA < NumOfPlayers - 1:
                        Striker = WicksA + 1
                    else:
                        print("All out!")
                        OverCounter = NumOfOvers
                        break
                if Check(ScoreA, ScoreB) == 1:
                    break
                balls_in_over += 1

            else:
                print("Enter Proper Input")

        if ListOfRunsGivenB[ListOfB.index(Bowler)] == 0:
            ListOfMaidensB[ListOfB.index(Bowler)] += 1
        ListOfOversB[ListOfB.index(Bowler)] += 1
        if Check(ScoreA, ScoreB) == 1:
            break

        OverCounter += 1


        # Swap at the end of the over only if the last run was not odd
        if Event not in ["1", "3", "5"]:
            Striker, NonStriker = Swap(Striker, NonStriker)

    print("Second Innings Ends")
    print(TeamA + " : " + str(ScoreA) + "/" + str(WicksA))
    Checker = Check(ScoreB, ScoreA)
    if Checker == 1:
        print(TeamB + " won by " + str(ScoreB - ScoreA) + " runs")
    elif Checker == 2:
        print(TeamA + " won by " + str(NumOfPlayers - 1 - WicksA) + " wickets")
    elif Checker == 0:
        print("Match is drawn")
    else:
        print("No Result")
    print("-----------------------------------------------------------------------------------")

# Displaying Score Card
print("SCORECARD")
print(TeamA + " - Batting")
print("-----------------------------------------------------------------------------------")
print("Player                                 Runs            SR           4's         6's")
print("-----------------------------------------------------------------------------------")
for i in range (0,len(ListOfA)):
    if (ListOfBallsPlayedA[i] != 0):
        print(ListOfA[i] + "("+ MOD_A[i] +")" + (40 - len(ListOfA[i]) - len(MOD_A[i]) - 2)*" " + str(ListOfScoresA[i]) + "(" +  str(ListOfBallsPlayedA[i]) + ")"
          + "          " + str(("%.1f" % ((ListOfScoresA[i]/ListOfBallsPlayedA[i])*100))) + "            " +
              str(ListOf4sA[i]) + "          " +  str(ListOf6sA[i]) )
    else:
        print(ListOfA[i] + "(DNP)" )
    print("-----------------------------------------------------------------------------------")

print(TeamA + " - " + str(ScoreA) + "/" + str(WicksA))
print()
print()
print(TeamB + " - Bowling")
print("-----------------------------------------------------------------------------------")

print("Player          Ovs        Runs     Wks       Economy")
print("-----------------------------------------------------------------------------------")

for i in range(0,len(ListOfB)):
    if (ListOfOversB[i] != 0):
        print(ListOfB[i] + (16 - len(ListOfB[i]))*" " + str(ListOfOversB[i]) + "          " + str(ListOfRunsGivenB[i]) + (10 - len(str(ListOfRunsGivenB[i]))) * " " +
        str(ListOfWicksB[i]) + "         "
          + str(ListOfRunsGivenB[i]/ListOfOversB[i]) + (15 - len(str(ListOfRunsGivenB[i]/ListOfOversB[i]))) * " ")
        print("-----------------------------------------------------------------------------------")

print()
print()
print(TeamB + " - Batting")
print("-----------------------------------------------------------------------------------")

print("Player                                 Runs            SR           4's         6's")
print("-----------------------------------------------------------------------------------")

for i in range (0,len(ListOfB)):
    if (ListOfBallsPlayedB[i] != 0):
        print(ListOfB[i] + "("+ MOD_B[i] +")" + (40 - len(ListOfB[i]) - len(MOD_B[i]) - 2)*" " + str(ListOfScoresB[i]) + "(" +  str(ListOfBallsPlayedB[i]) + ")"
          + "          " + str(("%.1f" % ((ListOfScoresB[i]/ListOfBallsPlayedB[i])*100))) + "            "+
        str(ListOf4sB[i]) + "           " +  str(ListOf6sB[i]) )
    else:
        print(ListOfB[i])
    print("-----------------------------------------------------------------------------------")
print(TeamB + " - " + str(ScoreB) + "/" + str(WicksB))
print()
print()
print(TeamA + " - Bowling")
print("-----------------------------------------------------------------------------------")

print("Player          Ovs        Runs       Wks       Economy     Mdns")
print("-----------------------------------------------------------------------------------")

for i in range(0,len(ListOfA)):
    if(ListOfOversA[i] != 0):
        print(ListOfA[i] + (16 - len(ListOfA[i]))*" " + str(ListOfOversA[i]) + "          " + str(ListOfRunsGivenA[i]) + (10 - len(str(ListOfRunsGivenA[i])))*" " +
              str(ListOfWicksA[i]) + "         "
          + str(ListOfRunsGivenA[i]/ListOfOversA[i]) + (15 - len(str(ListOfRunsGivenA[i]/ListOfOversA[i]))) * " ")
        print("-----------------------------------------------------------------------------------")
print()
print()
print("FINAL RESULT")

if ScoreA > ScoreB:
    if (Toss == TeamA and Decision_Toss == "Bat") or (Toss == TeamB and Decision_Toss == "Bowl"):
        print(TeamA + " won by " + str(ScoreA - ScoreB) + " runs.")
    else:
        print(TeamA + " won by " + str(NumOfPlayers - WicksA - 1) + " wickets.")
elif ScoreB > ScoreA:
    if (Toss == TeamA and Decision_Toss == "Bat") or (Toss == TeamB and Decision_Toss == "Bowl"):
        print(TeamB + " won by " + str(NumOfPlayers - WicksB - 1) + " wickets.")
    else:
        print(TeamB + " won by " + str(ScoreB - ScoreA) + " runs.")
else:
    print("Match is Draw")
print("-----------------------------------------------------------------------------------")


print("Thank you !")
