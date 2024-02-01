class Lion:
    def __init__(self, typed, sound):
        self.typed = typed
        self.sound = sound

    def movit(self):
        print("Walk")


class Human:
    def __init__(self, typed, sound):
        self.typed = typed
        self.sound = sound

    def movit(self):
        print("Crawl")


class Birds:
    def __init__(self, typed, sound):
        self.typed = typed
        self.sound = sound

    def movit(self):
        print("Fly")


simba = Lion("Carnivore", "Roar")
human = Human("Omnivore", "Cry")
ndege = Birds("Herbivore", "Quack")

for wanyama in (simba,human,ndege):
    print(wanyama.typed)
    print(wanyama.sound)
    wanyama.movit()
