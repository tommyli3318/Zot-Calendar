from course import Course

class Student:
	def __init__(self, name: str) -> None:
		#Creates and initializes a new stduent instance
		self.name = name
		self.courselist = [] #List of Course instances
	
	def _search(self, course_nm) -> "Course object":
		for c in self.courselist:
			if c.get_name() == course_nm:
				return c

	#Accessors and mutators for the student name
	def get_name(self) -> str:
		return self.name
	
	def set_name(self, new_name: str):
		self.name = new_name
	
	#Add an assignment 
	def add_grade(self, course_nm: str, a_nm: str, category: str, points_g: int, points_p: int) -> None:
		course_obj = self._search(course_nm)
		if course_obj == None:
			print("Course not found.") #Temporary error message if course isn't found
		else:
			course_obj.add_grade(a_nm, category, (points_g, points_p))
	
	def set_grade(self, course_nm: str, a_nm: str, category: str, n_points_g: int, n_points_p: int) -> None:
		course_obj = self._search(course_nm)
		if course_obj == None:
			print("Course not found.") #Temporary error message if course isn't found
		else:
			course_obj.set_grade(a_nm, category, (n_points_g, n_points_p))

	#Accessor for the grade. Compute the current grade of a course.
	def get_grade(self, course_nm: str) -> float:
		course_obj = self._search(course_nm)
		if course_obj == None:
			print("Course not found.") #Temporary error message if course isn't found
			return 0.0
		return course_obj.get_overall_score()
	
	#Add a course to the student's course list
	#PRE: len(categories) == len(weights) and len(categories) > 0
	def add_course(self, course_nm: str, categories: list, weights: list) -> None:
		cat_dict = {categories[i]: weights[i] for i in range(len(categories))}
		#for index in range(len(categories)):										#OBSOLETE
		#	cat_dict = {category: weights[index] for category in categories}		#OBSOLETE
		self.courselist.append(Course(course_nm, cat_dict))
	
	#Remove a course from the student's course list
	def remove_course(self, course_nm: str) -> None:
		course_obj = self._search(course_nm)
		if course_obj == None:
			print("Course not found.") #Temporary error message if course isn't found
		else:
			self.courselist.remove(course_obj)

	def add_task(self, course_nm: str, desc: str, m: int, d: int, y: int) -> None:
		# add a CourseTask object to Couse.to_do (a list)
		course_found = False
		for c in self.courselist:
			if c.get_name() == course_nm:
				c.add_task(desc,m,d,y)
				course_found = True
		if not course_found:
			print("Course not found.") #Temporary error message if course isn't found

	def get_to_do(self, course_nm):
		#for course
		pass




me = Student("Tedrick")
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
me.add_grade("Algorithm", "Amazing midterm", "Midterm", 75, 100)
me.add_grade("Algorithm", "Fucking kill me", "Final", 55, 100)
#testing set_grade
me.set_grade("Algorithm", "Amazing midterm", "Midterm", 100, 100)
me.add_grade("Algorithm", "Fucking kill me", "Final", 100, 100)

me.remove_course("Algorithm")

temp = me.get_grade("OChem")
print(f"me Ochem: {temp}")
temp2 = me.get_grade("Algorithm")
print(f"me Algorithm: {temp2}")



me2 = Student("Tedrick")
categories3 = ["Midterm", "Final", "Project"]
weights3 = [.25, .5, .25]
me2.add_course("OS", categories3, weights3)
me2.add_grade("OS", "Amazing midterm", "Midterm", 98, 100)
me2.add_grade("OS", "Amazing final", "Final", 86, 100)
me2.add_grade("OS", "Kernel assignment", "Project", 107, 100)

temp3 = me2.get_grade("OS")
print(f"me2 OS: {temp3}")