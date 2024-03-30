import random
import time

class Character:
    def __init__(self, hp, potion):
        self.hp = hp
        self.potion = potion

    def attack(self):
        damage = random.randint(50, 400)
        if damage > 300:
            print("CRITICAL HIT!")
        return damage

    def drink_potion(self):
        if self.potion > 0:
            potion = random.randint(30, 50)
            self.potion -= 1
            self.hp += potion
            return True
        else:
            print("sayang sekali potionmu habis!")
            return False

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_potion(self):
        return self.potion

    def set_potion(self, potion):
        self.potion = potion

#class keduanya
#Perulangan while

#fase naganya 
print("Selamat datang ke tugas kelompok 01 yang beranggota:")
print("Farrel Razaan Rabbani 21120123140108")
print("")
print("")
print("")
game = DragonCaveGame()
game.play()
