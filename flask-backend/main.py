import flask
from student import Student

app = flask.Flask("__main__")

#########################SAMPLE DATA#########################
categories = ["Exam", "Quiz", "Assignment", "Lab"]
weights = [.4, .3, .2, .1]

stu1 = Student("Tedrick")
categories3 = ["Midterm", "Final", "Project"]
weights3 = [.25, .5, .25]
stu1.add_course("OS", categories3, weights3)
stu1.add_grade("OS", "Amazing midterm", "Midterm", 98, 100)
stu1.add_grade("OS", "Amazing final", "Final", 86, 100)
stu1.add_grade("OS", "Kernel assignment", "Project", 107, 100)
stu1.add_task("OS", "reading 1", 2, 18, 2019)
stu1.add_task("OS", "reading 2", 2, 19, 2019)


stu1.add_course("OChem", categories, weights)
stu1.add_grade("OChem", "q 1", "Quiz", 98, 100)
stu1.add_grade("OChem", "Ass 1", "Assignment", 86, 100)
stu1.add_grade("OChem", "e 1", "Exam", 65, 100)
stu1.add_grade("OChem", "lab 1", "Lab", 80, 100)
stu1.add_task("OChem", "Chem r1", 2, 18, 2019)
stu1.add_task("OChem", "chem r3", 2, 20, 2019)
stu1.add_task("OChem", "chem r2", 2, 19, 2019)
stu1.add_task("OChem", "EXAM 1", 2, 20, 2019, "Exam", 2000)
stu1_rec = stu1.get_recommendations()

@app.route("/")
def my_index():
	return flask.render_template("index.html", token="aye", token2 = "testing2", rec1 = stu1_rec)


app.run(debug=True)