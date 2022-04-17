driving = input('請問你有沒有開過車?')
age = input('請問你的年齡?')
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
	    print('奇怪，你怎麼會有開過車')	