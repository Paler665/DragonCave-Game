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
class DragonCaveGame:
    def _init_(self):
        self.naga_baik = random.randint(1, 2)
        self.naga_jahat = 2 if self.naga_baik == 1 else 1
        self.kesempatan_kabur = random.randint(1, 50)

        self.player = Character(200, 4)
        self.naga = Character(2000, 0)

    def play(self):
        print("Kamu melihat dua gua di depanmu ...")
        time.sleep(1)
        gua = int(input("Apakah kamu memilih gua 1 atau 2?"))

        if gua == self.naga_baik:
            print("Gua ini gelap dan menakutkan…")
            time.sleep(1)
            print("Seekor naga besar muncul di depanmu! Ia membuka mulutnya dan...")
            time.sleep(1)
            print("Isi mulutnya berisi harta yang ingin dibagikan kepadamu, selamat kamu menemukan naga yang ramah")

        elif gua == self.naga_jahat:
            print("Naga itu mengeluarkan api dari mulutnya, dan kau hampir saja kena")
            time.sleep(1)
            decision = input("Apakah kau akan 'kabur' atau 'melawan' naga itu?")

            if decision == "kabur":
                if self.kesempatan_kabur >= 24:
                    print("Kamu berhasil kabur dari sergapan naga jahat itu")
                else:
                    print("Naga itu berhasil menangkapmu dan kau dibunuh")
                    return
            elif decision == "melawan":
                print("Sepertinya pedang yang kamu bawa berguna juga")
                time.sleep(1)
#Perulangan while

#fase naganya 
print("Selamat datang ke tugas kelompok 01 yang beranggota:")
print("Farrel Razaan Rabbani 21120123140108")
print("Maulana Yusuf Muhammad 21120123140166")
print("Aufa Ika Pramesti 21120123140139")
print("Ananda Dwiki Bayu Widiatama 21120123120026")
game = DragonCaveGame()
game.play()
