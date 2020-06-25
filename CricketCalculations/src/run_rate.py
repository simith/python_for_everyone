#calculate run rat
number_of_balls_per_over=6
runs=input("Enter the total runs:")
number_of_balls_bowled=input("Number of balls bowled:")

number_of_overs=int(number_of_balls_bowled)/number_of_balls_per_over
run_rate=(int(runs)/int(number_of_balls_bowled))
run_rate_per_over=(int(runs)/int(number_of_overs))

print("The team scored "+str(runs)+ " in "+ str(number_of_overs) + " overs and the run rate per over is:"+ str(run_rate_per_over))

#calculate projected score
number_of_balls_per_over=6

