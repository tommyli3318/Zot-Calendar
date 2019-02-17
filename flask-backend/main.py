import flask
from student import Student

app = flask.Flask("__main__")

#########################SAMPLE DATA#########################
categories = ["Exam", "Quiz", "Assignment", "Lab"]
weights = [.4, .3, .2, .1]

stu1 = Student("Tedrick")
categories3 = ["Midterm", "Final", "Project"]
weights3 = [.25, .5, .25]
stu1.add_course("English", categories3, weights3)
stu1.add_grade("English", "Amazing midterm", "Midterm", 98, 100)
stu1.add_grade("English", "Amazing final", "Final", 86, 100)
stu1.add_grade("English", "Kernel assignment", "Project", 107, 100)
stu1.add_task("English", "Reading Assignment 1", 2, 18, 2019)
stu1.add_task("English", "Reading Assignment 2", 2, 19, 2019)


stu1.add_course("OChem", categories, weights)
stu1.add_grade("OChem", "q 1", "Quiz", 98, 100)
stu1.add_grade("OChem", "Ass 1", "Assignment", 86, 100)
stu1.add_grade("OChem", "e 1", "Exam", 65, 100)
stu1.add_grade("OChem", "lab 1", "Lab", 80, 100)
stu1.add_task("OChem", "Chem Reading 3", 2, 18, 2019)
stu1.add_task("OChem", "Chem Reading 2", 2, 20, 2019)
stu1.add_task("OChem", "Chem Reading 1", 2, 19, 2019)
stu1.add_task("OChem", "EXAM 1", 2, 20, 2019, "Exam", 2000)
stu1_rec = stu1.get_recommendations()

print(stu1_rec)

@app.route("/")
def my_index():
	return flask.render_template("index.html", rec0 = stu1_rec[0], rec1 = stu1_rec[1], rec2 = stu1_rec[2],\
		rec3 = stu1_rec[3], rec4 = stu1_rec[4], rec5 = stu1_rec[5])


app.run(debug=True)