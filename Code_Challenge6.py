print ("Please fill up the following to get your Final Grades")

prelim = eval(input("Prelim Grade:"))
midterm = eval(input("Midterm Grade:"))
sfinals = eval(input("Semi-Finals Grade:"))
finals = eval(input("Finals Grade:"))
quiz = eval(input("Quiz Grade:"))
project = eval(input("Project Grade:"))

if (prelim >=65 and prelim <=100) and (midterm >=65 and midterm <=100) and (sfinals >=65 and sfinals <=100) and (finals >=65 and finals <=100) and (quiz >=65 and quiz <=100) and (project >=65 and project <=100):
	FG = (prelim * 0.15) + (midterm * 0.15) + (sfinals * 0.15) + (finals * 0.15) + (quiz * 0.15) + (project * 0.15)
	if FG >= 75:
		print (" Congratulations, you passed the course/subject ")
	else:
		print (" Sorry, better luck next time ")

else:
	print ("INVALID GRADE")