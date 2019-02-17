import flask
from student import Student
from flask import request
from flask_cors import cross_origin
import json

app = flask.Flask("__main__")

#########################SAMPLE DATA##########################

stu1 = Student("Tedrick")



EnglishCats = ["Midterm", "Final", "Project"]
EnglishWeights = [.25, .5, .25]

stu1.add_course("English", EnglishCats, EnglishWeights)
stu1.add_grade("English", "Amazing midterm", "Midterm", 98, 100)
stu1.add_grade("English", "Amazing final", "Final", 86, 100)
stu1.add_grade("English", "Kernel assignment", "Project", 107, 100)
stu1.add_task("English", "Reading Assignment 1", 2, 18, 2019)
stu1.add_task("English", "Reading Assignment 2", 2, 19, 2019)


MathCats = ["Exam", "Quiz", "Assignment", "Lab"]
MathWeights = [.4, .3, .2, .1]

stu1.add_course("Math", MathCats, MathWeights)
stu1.add_grade("Math", "q 1", "Quiz", 98, 100)
stu1.add_grade("Math", "Ass 1", "Assignment", 86, 100)
stu1.add_grade("Math", "e 1", "Exam", 65, 100)
stu1.add_grade("Math", "lab 1", "Lab", 80, 100)
stu1.add_task("Math", "Chem Reading 3", 2, 18, 2019)
stu1.add_task("Math", "Chem Reading 2", 2, 20, 2019)
stu1.add_task("Math", "Chem Reading 1", 2, 19, 2019)
stu1.add_task("Math", "EXAM 1", 2, 20, 2019, "Exam", 2000)



stu1_rec = stu1.get_recommendations()

def _helper(d):
	r_str = 'Priority list: \n\n'
	for item in d['hw']:
		r_str += f"{item}\n"
	return r_str

print(_helper(stu1_rec))

@app.route("/api/recs")
@cross_origin()
def my_index():
	return json.dumps(stu1_rec)

'''
u_input = ""
while not u_input == "quit":
	u_input = input("Enter an action: ag[add assignment grade], sg[set assignment grade], ac[add course], at[add task]: ")

	if u_input == "ag":
		student,course_nm,a_nm,category,points_g,points_p = input("Please enter 'Course Name, Assignment Name, Category, Points Gained, Points Available': ").rstrip().split(',')
		stu1.add_grade(course_nm,a_nm,category,points_g,points_p)

	elif u_input == "sg":
		student,course_nm,a_nm,category,points_g,points_p = input("Please enter 'Student Name, Course Name, Assignment Name, Category, Points Gained, Points Available': ").rstrip().split(',')
		stu1.set_grade(course_nm,a_nm,category,points_g,points_p)

	elif u_input == "ac":
		course_nm, MathCats, MathWeights = input("Please enter 'Course Name, Grading MathCats(list), Category MathWeights(list)': ").rstrip().split(',')
		stu1.add_course(course_nm, MathCats, MathWeights)

	elif u_input == "at":
		course_nm,desc,m,d,y,task_cat,points_p = input("Please enter 'Course Name, Description(str), m,d,y, task category (str), points possible': ").rstrip().split(',')
		stu1.add_task(course_nm,desc,m,d,y,task_cat,points_p)

	elif u_input == "g":
		stu1.get_recommendations()
'''
"""
@app.route("/api/info")
def my_index(id, methods=["POST"]):
	#data manipulation
	request.body
	return flask.render_template("index.html", rec0 = stu1_rec[0], rec1 = stu1_rec[1], rec2 = stu1_rec[2],\
		rec3 = stu1_rec[3], rec4 = stu1_rec[4], rec5 = stu1_rec[5])
"""

app.run(debug=True)