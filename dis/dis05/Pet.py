class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Dog(Pet):
    def __init__(self, name, owner, color):
        Pet.__init__(self, name, owner)
        self.color = color
    def talk(self):
        print(self.name + ' says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives
        self.is_alive = True
    def talk(self):
        """A cat says meow! when asked to talk."""
        print(self.name + ' says meow!')
    def lose_life(self):
        """A cat can only lose a life if they have at
        least one life. When lives reaches zero, 'is_alive'
        becomes False.
        """
        if self.lives > 0:
            self.lives -= 1
        if self.lives == 0:
            self.is_alive = False

class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    def talk(self):
        """Repeat what a Cat says twice."""
        super().talk()
        super().talk()


kitty = NoisyCat('Kitty', 'Human')
kitty.talk()
for i in range(9):
    kitty.lose_life()
    print(i + 1, kitty.is_alive)
