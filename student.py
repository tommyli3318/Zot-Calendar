import datetime

class Student:
	''' Creates a new course task with an associated deadline.
	PRE: The dates provided follow the format MMDDYYYY
	PRE: The provided dates are valid (i.e. not past dates!) '''
	def __init__(self, taskName: str, month: int, day: int, year: int) -> None:
		#Name of piece and its x,y coordinates
		self.taskName = taskName
		self.deadline = datetime.date(year, month, date)
		self.suggestedStartDate = deadline - datetime.timedelta(7)
	
	'''Accessors and mutators for the task type.'''
	def getTaskType(self):
		return self.taskName
	def setTaskType(self, newTaskType: str):
		self.taskName = newTaskType
	
	'''Accessors and mutators for the deadline. Note that the accessor
	returns the date in string format of ISO (YYYYMMDD). If any parameter
	for the mutator is 0, then do not change that field.
	
	PRE: The dates provided follow the format MMDDYYYY
	PRE: The provided dates are valid (i.e. not past dates!) '''
	def getDeadline(self):
		return self.deadline.strftime("%Y%m%d")
	def setDeadline(self, newmonth: int, newday: int, newyear: int):
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
	def getSuggestedStartDate(self):
		return self.suggestedStartDate.strftime("%Y%m%d")
	def setSuggestedStartDate(self, newmonth: int, newday: int, newyear: int):
		if newmonth != 0:
			self.suggestedStartDate.replace(month = newmonth)
		if newday != 0:
			self.suggestedStartDate.replace(day = newday)
		if newyear != 0:
			self.suggestedStartDate.replace(year = newyear)