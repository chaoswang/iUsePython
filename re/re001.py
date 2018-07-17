# !python3
# encoding=utf-8

def isPhone(num):
	if len(num) != 11:
		return False
	if not str.isdigit(num):
		return False
	li = ['138','137','136']
	if num[:3] not in li:
		return False
	return True

print(isPhone('13632934418'))

