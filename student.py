import datetime

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
	
	#Accessor for the grade. Compute the current grade of a course.
	def get_grade(self, course_name: str) -> float:
		for given_course in courselist:
			if given_course.get_name() == course_name:
				return given_course.compute_grade()
		print("Course not found.") #Temporary error message if course isn't found
		return 0.0
	
	#Add a course to the student's course list
	#PRE: len(categories) == len(weights) and len(categories) > 0
	def add_course(self, course_name: str, categories: list, weights: list) -> None:
		cat_dict = {categories[i]: weights[i] for i in range(len(categories))}
		#for index in range(len(categories)):										#OBSOLETE
		#	cat_dict = {category: weights[index] for category in categories}		#OBSOLETE
		self.courselist.append(course(course_name, cat_dict))
	