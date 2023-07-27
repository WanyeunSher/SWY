ss = 0
while ss < 100:
	ss = ss + 1
	if ss % 7 == 0 or ss % 10 == 7 or ss // 10 == 7:
	    continue
	else:
	    print(ss)
