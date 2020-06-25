#how to calculate bowlers economy rate
#economy rate=runs scored in bowlers over/overs bowled by bowler
number_of_balls_in_an_over=6
runs_scored_in_bowlers_overs=input("How many runs has the bowler conceded in his overs? ")
overs_bowled_by_bowler=input("How many overs has the bowler bowled?")

economy_rate=int(runs_scored_in_bowlers_overs)/int(overs_bowled_by_bowler)
economy_rate_per_ball = int(runs_scored_in_bowlers_overs)/(int(overs_bowled_by_bowler) * 6)
print("Economy rate per over: "+ str(economy_rate))
print("Economy rate per ball: "+ str(economy_rate_per_ball))

