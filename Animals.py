
class Animal:
  age = 0
  color = "white"

  def __init__(self):
    print("Animal is born")
    
  def move(self):
    print("Move")

  @staticmethod
  def help():
    print("Base class for all animals")




class Mammal(Animal):
  legs = 4
  eyes = 2

  def __init__(self):
    super().__init__()
    print("It is a mammal")

  def speak():
    print("Make a noise")
  
  def move(self):
    print("Walk")


class Dog(Mammal):
  def __init__(self):
    super().__init__()
    self.color = "brown"
    print("It is a Dog")

  def speak(self):
    print("Woof Woof")


class Cat(Mammal):
  def __init__(self):
    super().__init__()
    self.color = "tabby"
    print("It is a Cat")

  def speak(self):
    print("Meow")


class Bird(Animal):
  wings = 2
  legs = 2

  def __init__(self):
    super().__init__()
    self.color = "blue"
    print("It is a bird")

  def speak(self):
    print("Chirp Chirp")
  
  def move(self):
    print("Fly")


class Spider(Animal):
  legs = 8

  def __init__(self):
    super().__init__()
    self.color = "black"
    print("It is a spider")
  
  def move(self):
    print("Crawl")



def show_animal(animal):
  if hasattr(animal, "legs"):
    print("It has", animal.legs, "legs")
  if hasattr(animal, "wings"):
    print("It has", animal.wings, "wings")
  if hasattr(animal, "eyes"):
    print("It has", animal.eyes, "eyes")
  if hasattr(animal, "color"):
    print("It is", animal.color)
  if hasattr(animal, "move"):
    animal.move()
  if hasattr(animal, "speak"):
    animal.speak()


def main():
  
  Animal.help()
  print("#########")
  
  dog = Dog()
  show_animal(dog)
  print("#########")

  cat = Cat()
  show_animal(cat)
  print("#########")

  bird = Bird()
  show_animal(bird)
  print("#########")

  spider = Spider()
  show_animal(spider)
  print("#########")



if __name__ == "__main__":
  main()
