

import sys


n = 38

for x in range(n):
	grade = n

	if grade < 38: 
		print (grade)

	else:
		for i in range(3):
			if (grade+i) %5 == 0:
				new_grade = grade + i
print(new_grade)