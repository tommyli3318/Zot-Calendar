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

	def add_task(self, course_nm: str, desc: str, m: int, d: int, y: int, \
			task_cat: str = None, points_p = 0) -> None:
		# add a CourseTask object to Couse.to_do (a list)
		course_obj = self._search(course_nm)
		if course_obj == None:
			print("Course not found.") #Temporary error message if course isn't found
		else:
			course_obj.add_task(desc,m,d,y,task_cat,points_p)

	def get_to_do(self, course_nm, obj=False) -> list:
		course_obj = self._search(course_nm)
		if course_obj == None:
			print("Course not found.") #Temporary error message if course isn't found
		if obj:
			return course_obj.get_to_do_obj()
		return course_obj.get_to_do()

	def get_recommendations(self) -> str:
		lookup = {}
		course_grades = {}
		for course in self.courselist:
			lookup.update({x: 100 for x in self.get_to_do(course.get_name(), True)})
			course_grades[course.get_name()] = 100 * course.get_overall_score()
		# lookup is a dictionary of CourseTask object: number indicating urgency
		# higher urgency number == more important
		past_list = []
		for task in lookup:
			dl_diff = (task.get_dl_obj() - task.get_today()).days
			if dl_diff < 0:
				past_list.append(task)
			else:
				lookup[task] -= dl_diff
				# add a bunch of more uregency-modifying algorithms
				
				# modify urgency based on course grades
				lookup[task] += 3 * abs(course_grades[task.get_course()] % 10 - 5)

				# modify urgency based on assignment worth
				# simulate not doing the assignment, find out how much overall grade changes
				# ONLY IF the assignment has a valid category and obtainable points 
				# (e.g. reading assignments will not impact your grade)
				if task.get_task_cat() != None and task.get_pp() != 0:
					course_obj = self._search(task.get_course())
					if course_obj != None:
						sim_score = course_obj.get_simulated_score(task.get_task_cat(), task.get_pp())
						overall_diff = course_obj.get_overall_score() - sim_score
						lookup[task] += 50 * overall_diff

		for task in past_list:
			del lookup[task]

		rec_list = sorted(lookup, key= lambda x: -lookup[x])

		
		# x is a CourseTask object
		# rec_list = sorted(lookup, key= lambda x: int(x.get_deadline()))
		
		r_str = ""
		for rank,item in enumerate([str(x) for x in rec_list], 1):
			r_str += f"Priority {rank} --> {item}\n"

		return r_str



##########################TESTING RECOMMENDATION()#########################
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


#print(f'Student stu1 OS course grade: {stu1.get_grade("OS")}')
#print(f'Student stu1 OChem course grade: {stu1.get_grade("OChem")}')

#print(stu1.get_recommendations())
