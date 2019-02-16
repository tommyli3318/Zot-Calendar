import datetime

class course_task:
	''' Creates a new course task with an associated deadline.
	PRE: The dates provided follow the format MMDDYYYY
	PRE: The provided dates are valid (i.e. not past dates!) '''
	def __init__(self, task_name: str, month: int, day: int, year: int) -> None:
		self.task_name = task_name
		self.deadline = datetime.date(year, month, date)
		self.suggested_start_date = deadline - datetime.timedelta(7)
	
	'''Accessors and mutators for the task type.'''
	def get_task_type(self) -> str:
		return self.task_name
	def set_task_type(self, new_task_type: str):
		self.task_name = new_task_type
	
	'''Accessors and mutators for the deadline. Note that the accessor
	returns the date in string format of ISO (YYYYMMDD). If any parameter
	for the mutator is 0, then do not change that field.
	
	PRE: The dates provided follow the format MMDDYYYY
	PRE: The provided dates are valid (i.e. not past dates!) '''
	def get_deadline(self) -> str:
		return self.deadline.strftime("%Y%m%d")
	def set_deadline(self, newmonth: int, newday: int, newyear: int):
		if newmonth != 0:
			self.deadline.replace(month = newmonth)
		if newday != 0:
			self.deadline.replace(day = newday)
		if newyear != 0:
			self.deadline.replace(year = newyear)

	'''Accessors and mutators for the suggested start date. 
	Note that the accessor returns the date in string format of ISO (YYYYMMDD). 
	If any parameter for the mutator is 0, then do not change that field.
	
	PRE: The dates provided follow the format MMDDYYYY
	PRE: The provided dates are valid (i.e. not past dates!) '''
	def get_suggested_start_date(self) -> str:
		return self.suggested_start_date.strftime("%Y%m%d")
	def set_suggested_start_date(self, newmonth: int, newday: int, newyear: int):
		if newmonth != 0:
			self.suggested_start_date.replace(month = newmonth)
		if newday != 0:
			self.suggested_start_date.replace(day = newday)
		if newyear != 0:
			self.suggested_start_date.replace(year = newyear)