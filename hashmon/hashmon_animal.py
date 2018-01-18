import random

class Hashmon:
    def __init__(self, trainer, name='', attack=0, defense=0, hitpoints=0, special=0, speed=0):
        self.trainer = trainer
        self.name = name
        self.attack = attack
        self.defense = defense
        # Hitpoints can go down, max_hitpoints is constant.
        self.hitpoints = hitpoints
        self.max_hitpoints = hitpoints
        self.special = special
        self.speed = speed
        self.moves = {}
        # Critial hit stuff.
        self.critical_hit = ""
        self.critical = False
        
        self.status = "normal"
        self.level = 7
    
    def apply_poison(self, chance, opponent):
        if (chance > random.random()):
            opponent.status = "poisoned"
            return "{} was poisoned!".format(opponent.name)

        else:
            return ""

    def critical_chance(self, speed):
        random_number = random.randrange(0, 256)
        threshhold = speed
        self.critical = threshhold > random_number
        if self.critical:
            self.critical_hit = "CRITICAL HIT! "
        else:
            self.critical_hit = ""

    def attack_formula(self, level, attack_stat, attack_power, defense_stat, critical):
        
        # Constant.
        damage = 2
        # Attacking hashmon's level.
        damage *= self.level
        # Constant.
        damage /= 5
        # Constant.
        damage += 2
        # Attacker's "attack" stat.
        damage *= attack_stat
        # Ability's power stat.
        damage *= attack_power
        # Defender's "defense" stat.
        # Make sure not to divide my zero and implode the universe!
        if defense_stat > 0:
            damage /= defense_stat
        # Constant.
        damage /= 50
        # Constant.
        damage += 2
        
        # STAB - same-type attack bonus.
        #if attacker_type == attack_type:
        #    damage *= 1.5
        
        # Weakness / resistance goes here.
        #

        # Random number between 0.85 - 1.0.
        damage *= random.uniform(0.85, 1.0)

        if self.critical:
            damage *= ((2 * level) + 5) / (level + 5)

        return int(damage)
    
    def standard_damage(self, level, attack_power, opponent):
        self.critical_chance(self.speed)
        
        damage = self.attack_formula(level, self.attack, attack_power, opponent.defense, True)
        
        opponent.hitpoints -= damage

        reply = self.critical_hit + opponent.name + "'s HP fell to " + str(opponent.hitpoints) + '!'

        return damage, reply

    def high_crit_damage(self, level, attack_power, opponent):
        # 4 times the speed for high critical moves.
        self.critical_chance(self.speed * 4)
        
        damage = self.attack_formula(level, self.attack, attack_power, opponent.defense, True)

        opponent.hitpoints -= damage

        reply = self.critical_hit + opponent.name + "'s HP fell to " + str(opponent.hitpoints) + "!"

        return damage, reply

    def no_crit_damage(self, level, attack_power, opponent):
        # 0 speed for zero critical moves.
        self.critical_chance(0)

        damage = self.attack_formula(level, self.attack, attack_power, opponent.defense, True)

        opponent.hipoints -= damage

        reply = self.critical_hit + opponent.name + "'s HP fell to " + str(opponent.hitpoints) + "!"

        return damage, reply

    def move(self, opponent, move_name=None):
        self.critical = False
        self.critical_hit = ""
        
        print(self.name)
        print("Move name: {}".format(move_name))
        print("Hashmon has move: {}".format(move_name in self.moves))
        if move_name in self.moves:
            move = self.moves[move_name](opponent)
            move_name = move_name.upper()

        else:
            move = random.choice(list(self.moves.items()))
            move_name = move[0].upper()
            move = move[1](opponent)

        reply = "{} used {}! ".format(self.name, move_name)
        reply += move

        return reply

if __name__ == '__main__':
    nidoran = Hashmon('Nidoran', 14, 11, 25, 11, 13)
