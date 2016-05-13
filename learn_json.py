# -*- coding: utf-8 -*-
import json
import string,random
import os,datetime
class School():
	def __init__(self):
		self.name = random.choice(['SWJTU','MIT','Stanford','北京大学',u'unicode交通大学'])
		self.city = random.choice(['New York','Chengdu','London'])
		self.year = random.randint(1900,2016)
		self.info_arr = [self.name,self.city,self.year]

class Student():
	def __init__(self):
		self.name = self.name_gen()
		self.sex = random.choice(['Male','Female'])
		self.age = random.randint(10,70)
		self.school = School()
		self.info_arr = ['info',self.name,self.sex,self.age]

		# self.
	def __str__(self):
		return "name:%s,sex:%s,age:%d" %(self.name,self.sex,self.age)
	def name_gen(self):
		name = ""
		for i in range(random.randint(4,9)):
			name +=random.choice(string.letters)
		return name.capitalize()
	def sing(self):
		print "%s sing : la~la~la~" %(self.name)
	# def to_json(self):
	# 	return json.dumps(self.__dict__)

# class MyJSON():
# 	def __init__(self):
# 		self.students = self.gen_stu_obj(1000)
# 	def gen_stu_obj(self,num):
# 		students = []
# 		for i in  range(num):
# 			students.append(Student())
# 		return students
# 	def dumps(self):
# 		arr = []
# 		str = '['
# 		students = self.gen_stu_obj(100)
# 		for stu in students:
# 			arr.append(stu.to_json())
# 		for s in arr:
# 			str += s+','
# 		# return arr
# 		str +=']'
# 		return str


# 	def save_to_file(self,common_name='data',content='',file_type='.json'):
# 		content = self.dumps()

# 		str_now = datetime.datetime.now().strftime('%y%m%d %H-%M-%S')
# 		result_file_name = os.path.dirname(os.path.abspath(__file__)) +'\\'+common_name +str_now+file_type

# 		with open(result_file_name,"w") as result_file:
# 			result_file.write(content.encode('utf-8'))

# 		print "Saved to file: " + result_file_name

# 	def json_loads(self,arr):
# 		json_arr = []
# 		for item in arr:
# 			# print item
# 			# print json_loads(item)
# 			json_arr.append(json.loads(item))
# 		return json_arr
#写入当前文件夹下以时间命名的函数
def save_to_file(common_name,content,file_type='.json'):
	str_now = datetime.datetime.now().strftime('%y%m%d_%H-%M-%S')
	result_file_name = os.path.dirname(os.path.abspath(__file__)) +'\\'+common_name +str_now+file_type

	with open(result_file_name,"w") as result_file:
		result_file.write(content.encode('utf-8'))

	print "Saved to file: " + result_file_name
	return result_file_name
# j = MyJSON()
# print j.dumps()
# j.save_to_file()
# students = j.students
students = []
for i in range(0,100):
	students.append(Student())
# [Student()]*10
json_str = json.dumps(students,default = lambda o:o.__dict__,indent=4)
file_name = save_to_file('data',json_str,'.json')
# print json.dumps(students,default=lambda o:o.__dict__)
print file_name

f= file(file_name,'r')
stu_json = json.load(f)
print len(stu_json)
# print stu_json[0]

for stu in stu_json:
	print stu['school']['name']


