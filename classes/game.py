

import random


class Enemy:
    def __init__(self, hp, mp):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

    def get_hp(self):
        return self.hp


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKYELLOW = '\033[33m'


magic_color = [bcolors.FAIL, bcolors.OKYELLOW, bcolors.OKBLUE]

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def use_mp(self, cost):
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0
        return self.mp

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ":",magic_color[i - 1] + bcolors.BOLD + spell["name"]
                  + bcolors.ENDC, "(cost:", str(spell["cost"]) + ")")
            i += 1

