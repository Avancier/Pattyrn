# An interface for creating an object.

from pypattyrn.creational.factory import Factory # This is just an interface


class Cat(object):

	def speak(self):
		print('meow')

	
class Dog(object):

	def speak(self):
		print('woof')

	
class AnimalFactory(Factory):

	def create(self, animal_type):
		if animal_type == 'cat':
			return Cat()
		elif animal_type == 'dog':
			return Dog()
		else:
			return None

animal_factory = AnimalFactory()

cat = animal_factory.create('cat')
dog = animal_factory.create('dog')

cat.speak()	# 'meow'
dog.speak()	# 'woof'
