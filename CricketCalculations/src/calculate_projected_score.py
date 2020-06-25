#how to calculate projected score
number_of_balls_per_over=6
runs=input("Enter the total runs till now:")
number_of_balls_bowled=input("Number of balls bowled till now:")
total_number_of_overs=input("Total number of overs for the match:")
number_of_overs_bowled=int(number_of_balls_bowled)/int(number_of_balls_per_over)
number_of_overs_left=int(total_number_of_overs)-int(number_of_overs_bowled)
total_number_of_balls_left=int(total_number_of_overs*number_of_balls_per_over)-int(number_of_balls_bowled)
current_run_rate=int(runs)/int(number_of_overs_bowled)
projected_score=int(current_run_rate*number_of_overs_left)+int(runs)
print("Projected score: "+str(projected_score))


