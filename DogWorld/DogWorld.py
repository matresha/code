import random
from dognames import Names

class Dog():
	
	def __init__(self, name, age, gender):
		self.name = name
		self.gender = gender
		self.age = age
		self.pose = "standing"
		self.moving = False
		self.speed = 0
		self.bussy = False
		self.info = [name, age, gender]
		print(f"NEW DOG {', '.join(map(str, self.info))}")


	def sit(self):
		self.pose = "sitting"
		self.speed = 0
		print(self.name.title() + " is sitting")


	def stand(self):
		self.pose = "standing"
		self.speed = 0
		print(self.name.title() + " is standing")


	def walk(self):
		self.pose = "walking"
		self.speed = 1
		print(self.name.title() + " is walking")


	def run(self):
		self.pose = "running"
		self.speed = 3
		print(self.name.title() + " is running")

	def canPair(self, dog2):
		if self.age > 2 and not self.bussy:
			if dog2.gender == self.gender:
				return False
			if dog2.age < 3 or dog2.bussy:
				return False
			return True
		return False



def newDog():
	return Dog(random.choice(Names), 1, random.choice(["male", "female"]))


# def addAge(arr):
# 	for elem in arr:
# 		elem.age += 1


def pairing(arr):
	for elem in arr:
		for elem2 in arr:
			if elem.canPair(elem2):
				elem.bussy = True
				elem2.bussy = True
				for i in range(random.choice([1, 2, 3])):
					arr.append(newDog())
	for elem in arr:
		elem.age += 1
		elem.bussy = False


def die(arr):
	for elem in arr:
		if elem.age > 4 and elem.age <= 6:
			if random.choice([1, 2, 3, 4, 5, 6, 7, 8]) == 1:
				arr.remove(elem)
		if elem.age > 6 and elem.age <= 10:
			if random.choice([1, 2, 3, 4]) == 1:
				arr.remove(elem) 
		if elem.age > 10 and elem.age <= 14:
			if random.choice([1, 2]) == 1:
				arr.remove(elem)
		if elem.age > 14:
			arr.remove(elem)


def main():
	world = []
	
	for i in range(5):
		world.append(newDog())


	year = 0
	while world and year != 15:
		year += 1
		print(year)
		# addAge(world)
		pairing(world)
		die(world)

	print(len(world))



if __name__ == "__main__":
	main()










