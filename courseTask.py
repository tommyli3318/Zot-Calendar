from datetime import *

class CourseTask:
	''' Creates a new course task with an associated deadline.
	PRE: The dates provided follow the format MMDDYYYY
	PRE: The provided dates are valid (i.e. not past dates!) '''
	def __init__(self, course_nm: str, task_nm: str, month: int, day: int, year: int) -> None:
		self.course_nm = course_nm
		self.task_nm = task_nm
		self.deadline = date(year, month, day)
		self.suggested_start_date = self.deadline
	
	'''Accessors and mutators for the course/task names.'''
	def get_task_type(self) -> str:
		return self.task_nm
	def set_task_type(self, new_task_type: str):
		self.task_nm = new_task_type
	def get_course(self) -> str:
		return self.course_nm
	def set_course(self, new_course: str):
		self.course_nm = new_course
	

	'''Accessors and mutators for the deadline. Note that the accessor
	returns the date in string format of ISO (YYYYMMDD). If any parameter
	for the mutator is nonpositive, then do not change that field.
	
	PRE: The dates provided follow the format MMDDYYYY
	PRE: The provided dates are valid (i.e. not past dates!) '''
	def get_deadline(self) -> str:
		return self.deadline.strftime("%Y%m%d")

	def get_dl_obj(self) -> "Date object":
		return self.deadline

	def set_deadline(self, newmonth: int, newday: int, newyear: int):
		if newmonth > 0:
			self.deadline = self.deadline.replace(month = newmonth)
		if newday > 0:
			self.deadline = self.deadline.replace(day = newday)
		if newyear > 0:
			self.deadline = self.deadline.replace(year = newyear)

	'''Accessors and mutators for the suggested start date. 
	Note that the accessor returns the date in string format of ISO (YYYYMMDD). 
	If any parameter for the mutator is 0, then do not change that field.
	
	PRE: The dates provided follow the format MMDDYYYY
	PRE: The provided dates are valid (i.e. not past dates!) '''
	def get_suggested_start_date(self) -> str:
		return self.suggested_start_date.strftime("%m%d%Y")

	def get_today(self) -> "Date object":
 		return date.today()

	def __str__(self):
		return f'Task for course {self.course_nm}: {self.task_nm}, Due date: {self.deadline.strftime("%m/%d/%Y")}'




	# move this into student.py
	'''
	def set_suggested_start_date(self, newmonth: int, newday: int, newyear: int):
		if newmonth != 0:
			self.suggested_start_date.replace(month = newmonth)
		if newday != 0:
			self.suggested_start_date.replace(day = newday)
		if newyear != 0:
			self.suggested_start_date.replace(year = newyear)
	'''

if __name__ == "__main__":
	test1 = CourseTask("Intro to OS", "Kernel Assignment 1", 3, 2, 2019)
	test2 = CourseTask("Intro to OS", "Kernel Assignment 2", 3, 15, 2019)
	test3 = CourseTask("Intro to OS", "Mid term", 3, 19, 2019)
	print(test1.get_task_type())
	test2.set_task_type("Warmup Assignment 3")
	print(test2.get_task_type())
	print(test3.get_course())
	test3.set_course("Intro to A.I.")
	print(test3.get_course())
	print("Your homework is due on " + test1.get_deadline())
	test1.set_deadline(2, 15, 2019)
	print("Your homework is now due on " + test1.get_deadline())
	test1.set_deadline(4, 0, 0)
	print("Your new homework is now due on " + test1.get_deadline())