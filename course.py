#import CourseTask

class Course:
	"""contains all the information for a specific course"""
	def __init__(self, course_name: str, category_weights: dict) -> None:
		self.course_name = course_name
		self.category_weights = category_weights
		# self.cat_scores = {n:(0,0) for n in self.category_weights} # {category: (n,d)}
		self.assignments = {} #{(assignment_name, category) : (n,d)}
		self.to_do = []

	def get_name(self) -> str:
		return self.course_name

	def add_task(self, desc: str, dd: 'mmddyy') -> None:
		# add a CourseTask objct
		pass
		#self.to_do.append(CourseTask(taskName,dd[:2],dd[2:4],dd[4:]))

	def add_assignment(self, name: str, category: str, score: tuple) -> None:
		self.assignments[(name,category)] = score

	def remove_assignment(self, category: str, score: tuple) -> None:
		del self.assignments[(name,category)]

	def set_assignment(self, name: str, category: str, n_score: tuple) -> None:
		self.assignments[(name,category)] = n_score

	def get_overall_score(self) -> float:
		cat_scores = {n:[0,0] for n in self.category_weights} # {category: (n,d)}

		for nc, nd in self.assignments.items():
			cat_scores[nc[1]][0] += nd[0]
			cat_scores[nc[1]][1] += nd[1]

		for cat in cat_scores:
			if cat_scores[cat][1] == 0:
				cat_scores[cat] = 1.0
			else:
				cat_scores[cat] = cat_scores[cat][0]/cat_scores[cat][1]

		final_score = sum(cat_scores[cat] * self.category_weights[cat] for cat in cat_scores)
		return round(final_score, 3)

"""
testing = Course("math", {'homework': .3, 'tests': .7})
testing.add_assignment("assignment 1", "homework", (10,10))
testing.add_assignment("assignment 2", "homework", (5,10))
testing.add_assignment("test 1", "tests", (8,10))
print(testing.get_overall_score())
#final grade : 78.5
"""