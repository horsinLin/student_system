from show_menu import show
import re
import student

def main():
	isTrue = True  # 是否结束循环
	enterCount = 0  # 记录用户在选择处按回车的次数
	optCount = 0  # 记录选项选错次数
	while isTrue:
		show()  # 显示菜单
		try:
			opt = input("请选择：")
			opt_str = re.sub("\D","",opt)
			opt_int = int(opt_str)
		except Exception:
			enterCount += 1
			if enterCount == 5:
				print("请瑞雪使用学生信息管理系统，本次使用已结束！")
				print()
				break
			else:
				print("输入有误，请重新输入，谢谢！")
				print()
				continue
		else:
			if opt_int in range(0,8):
				if opt_int == 0:
					print("您已退出学生信息管理系统！")
					isTrue = False
				elif opt_int == 1:
					student.insert()
				elif opt_int == 2:
					student.search()
				elif opt_int == 3:
					student.delete()
				elif opt_int == 4:
					student.modify()
				elif opt_int == 5:
					student.sort()
				elif opt_int == 6:
					student.total()
				elif opt_int == 7:
					student.show()
			else:
				optCount += 1
				if optCount == 5:
					print("选择错误次数过多，怀疑您在恶意使用系统，本次使用已结束！")
					print()
					break
				else:
					print("请选择正确的选项，谢谢！")
					print()
					continue

if __name__ == '__main__':
	main()