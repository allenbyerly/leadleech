f = open('leadlist.txt', "r")

lines = f.readlines()
f.close()

for line in lines:
	#print line
	text = line.strip()
	print text
