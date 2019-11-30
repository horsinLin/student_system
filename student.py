import os

filename = "student_txt.txt"  # 存放用户信息的本地文件

def save(students):
	try:
		student_txt = open(filename,"a")
	except Exception as e:
		student_txt = open(filename,"w")
	finally:
		for student in students:
			student_txt.write(str(students)+"\n")
		student_txt.close()

# 录入学生信息
def insert():
	stuList = []  # 用于存放用户字典
	isTrue = True  # 标记是否继续添加用户
	while isTrue:
		id = input("请输入ID(如：1001)：")
		if not id:
			break
		name = input("请输入名字：")
		if not name:
			break
		try:
			english = int(input("请输入英语成绩："))
			python = int(input("请输入Python成绩："))
			c = int(input("请输入C语言成绩："))
		except Exception:
			print("输入了无效的成绩，请重新输入！")
			continue
		else:
			# 将学生信息保存到字典
			stuInfo = {"id": id, "name": name,\
			"english": english, "python": python,\
			"c": c}
			# 将学生字典添加到列表中
			stuList.append(stuInfo)
			isAdd = input("是否继续添加信息？(y/n)：")
			if isAdd == "y":
				isTrue = True
			else:
				isTrue = False
	# 保存用户本地
	save(stuList)
	print("学生信息录入完毕！")

def show_student(student_query,mode=0):
	with open(filename,"r") as file:
		student = file.readlines()
		if mode == 1:  # 通过id查询并显示
			for list in student:
				if not student_query:
					print("检测不到您输入任何信息，请重新输入！")
				else:
					d = dict(eval(list))
					if student_query == d["id"]:
						print("+--------+----------+-------------+------------+-------+")
						print("|   id   |   name   |   english   |   python   |   c   |")
						print("+--------+----------+-------------+------------+-------+")
						print("|%s|%s|%s|%s|%s|"%(d["id"].center(8),\
												  d["name"].center(10),\
												  str(d["english"]).center(13),\
												  str(d["python"]).center(12),\
												  str(d["c"]).center(7)))
						print("+--------+----------+-------------+------------+-------+")
						break
					else:
						print("没有找到相关学生的信息")
						break
		elif mode == 2:  # 通过姓名查询并显示
			for list in student:
				if not student_query:
					print("检测不到您输入任何信息，请重新输入！")
				else:
					d = dict(eval(list))
					if student_query == d["name"]:
						print("+--------+----------+-------------+------------+-------+")
						print("|   id   |   name   |   english   |   python   |   c   |")
						print("+--------+----------+-------------+------------+-------+")
						print("|%s|%s|%s|%s|%s|"%(d["id"].center(8),\
												  d["name"].center(10),\
												  str(d["english"]).center(13),\
												  str(d["python"]).center(12),\
												  str(d["c"]).center(7)))
						print("+--------+----------+-------------+------------+-------+")
						break
					else:
						print("没有找到相关学生的信息")
						break
		else:
			students = []  # 存放学生信息字典
			for student in student_query:
				if mode == 0:
					student = dict(eval(student))
				students.append(student)
			print("+--------+----------+-------------+------------+-------+")
			print("|   id   |   name   |   english   |   python   |   c   |")
			print("+--------+----------+-------------+------------+-------+")
			for student in students:
				print("|%s|%s|%s|%s|%s|" % (student["id"].center(8), \
											student["name"].center(10), \
											str(student["english"]).center(13), \
											str(student["python"]).center(12), \
											str(student["c"]).center(7)))
			print("+--------+----------+-------------+------------+-------+")

# 查询
def search():
	isTrue = True  # 是否继续查询
	while isTrue:
		if os.path.exists(filename):
			try:
				mode = int(input("1.按学生ID查询；2.按姓名查询；(1/2):"))
			except Exception:
				print("请输入数字1或者数字2，谢谢！")
				continue
			else:
				if mode == 1:
					stuId = input("请输入学生的ID：")
					show_student(stuId.strip(),mode)
					while True:
						isCon = input("是否继续查询？（y/n）")
						if isCon == "y":
							isTrue = True
							break
						elif isCon == "n":
							print("本次查询结束！")
							isTrue = False
							break
						else:
							print("请输入 y 或 n ！")
							continue
				elif mode == 2:
					stuName = input("请输入学生的姓名：")
					show_student(stuName.strip(),mode)
					while True:
						isCon = input("是否继续查询？（y/n）")
						if isCon == "y":
							isTrue = True
							break
						elif isCon == "n":
							print("本次查询结束！")
							isTrue = False
							break
						else:
							print("请输入 y 或 n ！")
							continue
				else:
					print("请输入数字1或者数字2，谢谢！")
		else:
			print("目前没有找到任何学生信息，无法进行此操作！")
			isTrue = False

# 删除学生信息
def delete():
	isTrue = True  # 是否继续删除
	while isTrue:
		if os.path.exists(filename):
			stuID = input("请输入要删除学生ID：")
			if not stuID:
				print("由于您没有输入相关学生的ID，本次操作结束！")
				break
			else:
				# 读取学生信息保存到student_old中
				with open(filename,"r") as rfile:
					student_old = rfile.readlines()
		else:
			student_old = []
		isDel = False  # 是否删除
		if student_old:
			with open(filename,"w") as wfile:
				for student in student_old:
					# 将学生字符串转出字典
					student = dict(eval(student))
					if student["id"] != stuID:
						wfile.write(str(student)+"\n")
					else:
						isDel = True
				if isDel:
					print("您已将ID为 %s 的学生相关信息成功删除！"%stuID)
					isConDel = input("是否继续删除？(y/n)")
					if isConDel == "y":
						isTrue = True  # 继续删除
					else:
						isTrue = False # 退出删除学生信息功能
				else:
					print("没有找到ID为 %s 的学生信息，删除失败！"%stuID)
		else:
			print("目前没有找到任何学生信息，无法进行此操作！")
			isTrue = False

# 修改
def modify():
	isTrue = True
	while isTrue:
		# 判断文件是否存在
		if os.path.exists(filename):
			stuID = input("请输入要修改的学生ID：")
			if not stuID:
				print("由于您没有输入相关学生的ID，本次操作结束！")
				break
			else:
				# 读取学生信息保存到student_old中
				with open(filename,"r") as rfile:
					student_old = rfile.readlines()
		else:
			student_old = []
		if student_old:
			with open(filename,"w") as wfile:
				for student in student_old:
					# 将学生字符串转出字典
					student = dict(eval(student))
					if student["id"] != stuID:
						wfile.write(str(student)+"\n")
					else:
						print("查询到到该学生，请修改该学生以下相关信息")
						while True:
							try:
								student["id"] = input("请输入学生新的ID:")
								student["name"] = input("请输入学生新的姓名：")
								student["english"] = int(input("请输入新的英语成绩："))
								student["python"] = int(input("请输入新的Python成绩："))
								student["c"] = int(input("请输入新的C语言成绩："))
							except Exception:
								print("输入有错误，请核对后再输入")
								continue
							else:
								wfile.write(str(student)+"\n")
								print("学生信息修改成功！")
								isConMod = input("是否要继续修改学生信息？(y/n)")
								# 是否继续修改学生信息
								if isConMod == "y":
									isTrue = True
								else:
									isTrue = False
								break
		else:
			print("目前没有找到任何学生信息，无法进行此操作！")
			isTrue = False

# 排序
def sort():
	if os.path.exists(filename):
		student_new = []
		with open(filename,"r") as file:
			student_old = file.readlines()
			for student in student_old:
				student = dict(eval(student))
				student_new.append(student)
		while True:
			ascORdecs = input("请选择(0.升序；1.降序)：")
			if ascORdecs == "0":
				ascORdecsBool = False
				break
			elif ascORdecs == "1":
				ascORdecsBool = True
				break
			else:
				print("请选择 0 或 1 ！")
				continue
		while True:
			mode = input("请选择排序方式：(1.按英语成绩排序；2.按python成绩排序；3.按C语言成绩排序；4.按总成绩排序）：")
			if mode == "1":
				student_new.sort(key=lambda x: x["english"], reverse=ascORdecsBool)
				break
			elif mode == "2":
				student_new.sort(key=lambda x: x["python"], reverse=ascORdecsBool)
				break
			elif mode == "3":
				student_new.sort(key=lambda x: x["c"], reverse=ascORdecsBool)
				break
			elif mode == "4":
				student_new.sort(key=lambda x: x["english"]+x["python"]+x["c"],\
								 reverse=ascORdecsBool)
				break
			else:
				print("输入有误，请重新输入！")
				continue
		show_student(student_new,mode=3)
	else:
		print("目前没有任何学生信息，无法完成此操作！")

def total():
	if os.path.exists(filename):
		with open(filename,"r") as file:
			student = file.readlines()
			if len(student) == 0:
				print("目前没有任何学生信息")
			else:
				print("一共有 %d 名学生！"%len(student))
	else:
		print("目前没有任何学生信息！")

def show():
	if os.path.exists(filename):
		with open(filename,"r") as file:
			student = file.readlines()
			if len(student) == 0:
				print("目前还没有任何学生信息")
			else:
				show_student(student)
	else:
		print("目前还没有任何学生信息，无法进行此操作")