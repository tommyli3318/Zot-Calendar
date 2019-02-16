import datetime

class student:
	''' Creates and initializes a new stduent instance'''
	def __init__(self, name: str) -> None:
		self.name = name
		self.courselist = [] #List of Course instances
		
	'''Accessors and mutators for the student name.'''
	def get_name(self):
		return self.name
	def set_name(self, new_name: str):
		self.name = new_name
	
	'''Accessor for the grade'''
	def get_grade(self, course_name: str):
		for given_course in courselist:
			if given_course.get_name() == course_name:
				return given_course.compute_grade()
		print("Course not found.") #Temporary error message if course isn't found
		return 0.0
	
	