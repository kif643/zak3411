class Animals:
    def __init__(self,name,eat,age,mood):
        self.name = name
        self.eat = eat
        self.age = age
        self.mood = mood
    def info(self):
        print(f'name={self.name}')
        print(f'eat={self.eat}')
        print(f'age={self.age}')
        print(f'mood={self.mood}')
print('\nCat:')
Cat=Animals('Barsik','Royal Chain',3,'sleepy')
Cat.info()
class Dog(Animals):
    def __init__(self,name,eat,age,mood):
        super().__init__(name,eat,age,mood)
    def info(self):
        super().info()
print('\nDog:')
Byblik=Dog('Byblik','Royal Chain',2,'good')
Byblik.info()
class Parrot(Animals):
    def __init__(self,name,eat,age,mood):
        super().__init__(name,eat,age,mood)
    def info(self):
        super().info()
print('\nParrot:')
Kesha=Parrot('Kesha','Rio',1,'sadly')
Kesha.info()