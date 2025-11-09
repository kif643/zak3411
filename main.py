class Dog:
    def __init__(self,name,age,sleep,breed,feed):
        self.name = name
        self.age = age
        self.sleep = sleep
        self.breed = breed
        self.feed = feed
    def print_info(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')
        print(f'sleep: {self.sleep}')
        print(f'breed: {self.breed}')
        print(f'feed: {self.feed}')
Byblik=Dog(name='Byblik',age='2',sleep='5',breed='pug',feed='Royal Canin')
Byblik.print_info()
def grow(self):
    self.age += 1
    self.sleep += 1
    self.mood -=1
    self.feed -= 1
    self.weight += 1
    self.games -=1
class Cat:
    def __init__(self,name,age,sleep,breed,feed,mood,weight,games):
        self.name = name
        self.age = age
        self.sleep = sleep
        self.breed = breed
        self.feed = feed
        self.mood = mood
        self.weight = weight
        self.games = games
    def print_info(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')
        print(f'sleep: {self.sleep}')
        print(f'breed: {self.breed}')
        print(f'feed:{self.feed}')
        print(f'mood: {self.mood}')
        print(f'weight: {self.weight}')
        print(f'games: {self.games}')
    def grow(self):
        self.age += 1
        self.sleep += 1
        self.mood-= 1
        self.feed -= 1
        self.weight += 1
        self.games -= 1
Keksik=Cat(name='Keksik',age='4',sleep='7',breed='british cat',feed='Leonardo Pienso',weight=10,games=5,mood=5)
Keksik.print_info()




