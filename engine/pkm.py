
class Pokemon:
    def __init__(self, name, nickname, lvl, hpt, hp):
        self.name = name
        self.nickname = nickname if nickname else name
        self.lvl = lvl
        self.hp = hp    # HP atual
        self.hpt = hpt  # HP total/original
    
    def damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, heal):
        self.hp += heal
        if self.hp > self.hpt:
            self.hp = self.hpt
        return self.hp


if __name__ == "__main__":
    
    pikachu = Pokemon(name="Pikachu", nickname="Bono do U2", lvl=5, hpt=35, hp=35)
    print(f"{pikachu.nickname} - HP: {pikachu.hp}/{pikachu.hpt}")

    pikachu.damage(10)
    print(f"{pikachu.nickname} sofreu 10 de dano - HP: {pikachu.hp}/{pikachu.hpt}")

    pikachu.heal(5)
    print(f"{pikachu.nickname} foi curado em 5 - HP: {pikachu.hp}/{pikachu.hpt}")

    pikachu.damage(40)
    print(f"{pikachu.nickname} sofreu 40 de dano - HP: {pikachu.hp}/{pikachu.hpt}")

    pikachu.heal(50)
    print(f"{pikachu.nickname} foi curado em 50 - HP: {pikachu.hp}/{pikachu.hpt}")
    
    
