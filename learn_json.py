import json
import string,random



class Student():
	def __init__(self):
		self.name = self.name_gen()
		self.sex = random.choice(['Male','Female'])
		self.age = random.randint(10,70)
		self.
	def __str__(self):
		return "name:%s,sex:%s,age:%d" %(self.name,self.sex,self.age)
	def name_gen(self):
		name = ""
		for i in range(random.randint(4,9)):
			name +=random.choice(string.letters)
		return name.capitalize()
	def sing(self):
		print "%s sing : la~la~la~" %(self.name)
	def to_json(self):
		return json.dumps(self.__dict__)

# def name_gen():
# 	name = ""
# 	for i in range(random.randint(4,9)):
# 		name +=random.choice(string.letters)
# 	return name.capitalize()

# print name_gen()

students = []
for i in range(100):
 students.append(Student())
js = []
for s in students:
	js.append(s.to_json())
	# print s.to_json()
print js	
# j_str = json.dumps(students.__dict__)
# print j_str

def json_loads(arr):
	json_arr = []
	for item in arr:
		# print item
		# print json_loads(item)
		json_arr.append(json.loads(item))
	return json_arr
# new_students = json_loads(js)
# print len(new_students)
# st

# for s in new_students:
# 	print s.name
# print json_loads(js)

