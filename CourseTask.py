import datetime;
#import java.util.GregorianCalendar;

class CourseTask:
	''' Creates a new course task with an associated deadline.
	PRE: The dates provided follow the format MMDDYYYY
	PRE: The provided dates are valid (i.e. not past dates!) '''
	def __init__(self, taskName, month, day, year):
		#Name of piece and its x,y coordinates
		self.taskName = taskName
		self.deadline = datetime.date(year, month, date)
		self.suggestedStartDate = deadline - datetime.timedelta(7)
	
	'''Accessors and mutators for the task type.'''
	def getTaskType(self):
		return self.taskName
	def setTaskType(self, newTaskType):
		self.taskName = newTaskType
	
	'''Accessors and mutators for the deadline. Note that the accessor
	returns the date in string format of ISO (YYYYMMDD). If any parameter
	for the mutator is 0, then do not change that field.
	
	PRE: The dates provided follow the format MMDDYYYY
	PRE: The provided dates are valid (i.e. not past dates!) '''
	def getDeadline(self):
		return self.deadline.strftime("%Y%m%d")
	def setDeadline(self, newmonth, newday, newyear):
		if newmonth != 0:
			self.deadline.replace(month = newmonth)
		if newday != 0:
			self.deadline.replace(day = newday)
		if newyear != 0:
			self.deadline.replace(year = newyear)

	public GregorianCalendar getDeadline()
	{
		return this.deadline;
	}
	public void setTaskType(int month, int day, int year)
	{
		this.deadline.set(year, month, day);
	}
	
	/*
	 * Accessors and mutators for the suggested start date.
	 * 
	 * PRE: The dates provided follow the format MMDDYYYY
	 * PRE: The provided dates are valid (i.e. not past dates!)
	 */
	public GregorianCalendar getSuggestedStartDate()
	{
		return this.suggestedStartDate;
	}
	public void setSuggestedStartDate(int month, int day, int year)
	{
		this.suggestedStartDate.set(year, month, day);
	}

}