from course import Course

class student:
	def __init__(self, name: str) -> None:
		#Creates and initializes a new stduent instance
		self.name = name
		self.courselist = [] #List of Course instances
		
	#Accessors and mutators for the student name.
	def get_name(self) -> str:
		return self.name
	def set_name(self, new_name: str):
		self.name = new_name
	
	#Add an assignment 
	def add_grade(self, course_name: str, assignment_name: str, category: str, points_gained: int, points_possible: int):
		course_found = False
		for given_course in self.courselist:
			if given_course.get_name() == course_name:
				given_course.add_assignment(assignment_name, category, (points_gained, points_possible))
				course_found = True
		if not course_found:
			print("Course not found.") #Temporary error message if course isn't found
	
	#Accessor for the grade. Compute the current grade of a course.
	def get_grade(self, course_name: str) -> float:
		for given_course in self.courselist:
			if given_course.get_name() == course_name:
				return given_course.get_overall_score()
		print("Course not found.") #Temporary error message if course isn't found
		return 0.0
	
	#Add a course to the student's course list
	#PRE: len(categories) == len(weights) and len(categories) > 0
	def add_course(self, course_name: str, categories: list, weights: list) -> None:
		cat_dict = {categories[i]: weights[i] for i in range(len(categories))}
		#for index in range(len(categories)):										#OBSOLETE
		#	cat_dict = {category: weights[index] for category in categories}		#OBSOLETE
		self.courselist.append(Course(course_name, cat_dict))
	
	#Remove a course from the student's course list
	def remove_course(self, course_name: str, categories: list, weights: list) -> None:
		for given_course in self.courselist:
			if given_course.get_name() == course_name:
				self.remove(given_course)
		print("Course not found.") #Temporary error message if course isn't found



me = student("Tedrick")
print("The name is " + me.get_name())
me.set_name("Nathan")
print("The new name is " + me.get_name())

categories = ["Exam", "Quiz", "Assignment", "Lab"]
weights = [.4, .3, .2, .1]
me.add_course("OChem", categories, weights)
me.add_grade("OChem", "Midterm1", "Exam", 77, 100)
me.add_grade("OChem", "Midterm2", "Exam", 44, 100)
me.add_grade("OChem", "Essay", "Assignment", 88, 97)
me.add_grade("OChem", "Pop quiz 1", "Quiz", 3, 5)
me.add_grade("OChem", "Pop quiz 2", "Quiz", 4, 5)
me.add_grade("OChem", "Pop quiz 3", "Quiz", 4, 6)
me.add_grade("OChem", "Distillation lab", "Lab", 10, 10)

categories2 = ["Midterm", "Final"]
weights2 = [.5, .5]
me.add_course("Algorithm", categories2, weights2)
me.add_grade("Algorithm", "Amazing midterm", "Exam", 75, 100)
me.add_grade("Algorithm", "Fucking kill me", "Exam", 55, 100)

print(me.get_grade("OChem"))
print(me.get_grade("Algorithm"))



me2 = student("Tedrick")
categories3 = ["Midterm", "Final", "Project"]
weights3 = [.25, .5, .25]
me.add_course("OS", categories3, weights3)
me.add_grade("OS", "Amazing midterm", "Midterm", 98, 100)
me.add_grade("OS", "Amazing final", "Final", 86, 100)
me.add_grade("OS", "Kernel assignment", "Project", 107, 100)
print(me2.get_grade("OS"))