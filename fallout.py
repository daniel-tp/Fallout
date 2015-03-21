import random
content = open("enable1.txt").readlines()
length = 4
amount = 5
words = []
realpass = 0
while True:
	s = input("Difficulty level? (1-5): ")
	if int(s) >=1 and int(s)<=5:
		length+=int(s)
		amount=(2*int(s))+2
		break
	else:
		print("actual difficulty please")
for item in content:
	if len(item) == length+1:
		words.append(item.rstrip())

passwords = random.sample(words, amount)
print("FIND THE RIGHT PASSWORD");
realpass = random.randrange(len(passwords))
for item in passwords:
	print(item.upper())
	tries = 4
while True:
	s = input('Guess: ')
	s = s.lower();
	if s == passwords[realpass]:
		print("Congratulations. You won with %d tries left!"%tries)
		break
	elif s in passwords:
		correct = 0
		for charnum in range(len(s)):
			if s[charnum] == passwords[realpass][charnum]:
				correct+=1
		print("%d/%d correct" % (correct, length))
		tries -=1
		print("%d tries left" % tries)
		if tries == 0:
			print ("GAME OVER!")
			break
		
	else:
		print("Wrong input")