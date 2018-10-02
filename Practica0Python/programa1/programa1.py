import random

try:
	number=int(input("Number:"))
except ValueError:
	print("This is not a number.")

random = random.randint(1,100)
#print("Number random:"+str(random))

while random != number:
	if random < number:
		print("The number random is less")
	elif random > number:
		print("The number random is higher")
	number=int(input("Enter your number:"))

print("Congratulation!")
