class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
    def add_hero(self, hero):
            self.heroes.append(hero)

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
        

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    


if __name__ == "__main__":
    print('hello')
