import random
import sys

for i in range(int(sys.argv[1])):
	f = open('nums.txt' + str(i), 'w')

	for _ in range (100):
		num = random.randint(1,pow(10,10))
		f.write(str(num) + '\n')

	print "finished writing"
