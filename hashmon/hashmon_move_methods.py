from collections import OrderedDict
import random

def bubble(self, opponent):
    damage, reply = self.standard_damage(self.level, 20, opponent)

    if random.randrange(1, 10) == 10:
        opponent.speed -= 13
        if opponent.speed < 0:
            opponent.speed = 0
        reply += " " + opponent.name + "'s SPD fell to " + str(opponent.speed) + "!"

    return reply

def bite(self, opponent):
    damage, reply = self.standard_damage(self.level, 20, opponent)
        
    return reply

def leech_life(self, opponent):
    # This is for accuracy.
    #if (1.0 > random.random()):
    damage, reply = self.standard_damage(self.level, 15, opponent)
    
    restore = int(damage / 2)
    self.hitpoints += restore
    if self.hitpoints > self.max_hitpoints:
        self.hitpoints = self.max_hitpoints
        
    reply += " " + self.name + "'s HP rose to " + str(self.hitpoints) + "!"

    return reply

def harden(self, opponent):
    self.defense += 13

    return "{}'s DEF rose to {}!".format(self.name, str(self.defense))

def agility(self, opponent):
    self.speed += 13

    return "{}'s SPD rose to {}!".format(self.name, str(self.speed))

def string_shot(self, opponent):
    opponent.speed -= 13
    if opponent.speed < 0:
        opponent.speed = 0

    return "{}'s SPD fell to {}!".format(opponent.name, opponent.speed)

def rock_slide(self, opponent):
    if (0.75 > random.random()):
        damage, reply = self.standard_damage(self.level, 50, opponent)
    
    else:
        reply = "It missed! "

    return reply

def dragon_rage(self, opponent):
    opponent.hitpoints -= 6

    return "{}'s HP fell to {}!".format(opponent.name, str(opponent.hitpoints))

def seismic_toss(self, opponent):
    opponent.hitpoints -= self.level

    return "{}'s HP fell to {}!".format(opponent.name, opponent.hitpoints)

def submission(self, opponent):
    if (0.8 > random.random()):
        damage, reply = self.standard_damage(self.level, 50, opponent)
        self.hitpoints -= int(damage * 0.25) + 1
        reply += " {}'s HP fell to {}".format(self.name, str(self.hitpoints))
    else:
        reply = "It missed! "

    return reply

def jump_kick(self, opponent):
    if (0.9 > random.random()):
        damage, reply = self.standard_damage(self.level, 50, opponent)
        return reply
    else:
        self.hitpoints -= 1
        reply = "It missed! {}'s HP fell to {}! ".format(self.name, str(self.hitpoints))
        return reply

def horn_drill(self, opponent):
    if self.speed > opponent.speed:
        if (0.1 > random.random()):
            opponent.hitpoints -= opponent.hitpoints
            reply = "OHKO! {}'s HP fell to {}! ".format(opponent.name, str(opponent.hitpoints))
            return reply

        else:
            return "It missed! "

    else:
        return "No effect! "

def recover(self, opponent):
    self.hitpoints += 7
    if self.hitpoints > self.max_hitpoints:
        self.hitpoints = self.max_hitpoints

    return "{}'s HP rose to {}!".format(self.name, str(self.hitpoints))

def night_shade(self, opponent):
    opponent.hitpoints -= self.level

    return "{}'s HP fell to {}!".format(opponent.name, str(opponent.hitpoints))

def poison_sting(self, opponent):
    damage, reply = self.standard_damage(self.level, 15, opponent)
    reply += self.apply_poison(0.2, opponent)

    return reply

def acid(self, opponent):
    damage, reply = self.standard_damage(self.level, 40, opponent)

    if (0.3 > random.random()):
        opponent.defense -= 13 
        if opponent.defense < 0:
            opponent.defense = 0

        reply += " {}'s DEF fell to {}!".format(opponent.name, str(opponent.defense))

    return reply

def poison_powder(self, opponent):
    reply = self.apply_poison(0.75, opponent)

    if not reply:
        reply = "It missed! "

    return reply

def toxic(self, opponent):
    reply = self.apply_poison(1.0, opponent)
    
    if not reply:
        reply = "It missed! "

    return reply

def smog(self, opponent):
    reply = ""

    if (0.7 > random.random()):
        damage, reply = self.standard_damage(self.level, 30, opponent)
        
        poison = self.apply_poison(0.4, opponent)
        if poison:
            reply += poison
    
    else:
        reply = "It missed! "

    return reply

def sludge(self, opponent):
    damage, reply = self.standard_damage(self.level, 65, opponent)
        
    poison = self.apply_poison(0.4, opponent)
    if poison:
        reply += poison
    
    return reply

def poison_gas(self, opponent):
    reply = self.apply_poison(0.55, opponent)

    if not reply:
        reply = "It missed! "

    return reply

def lick(self, opponent):
    damage, reply = self.standard_damage(self.level, 30, opponent)

    if (0.3 > random.random()):
        opponent.status = "paralyzed"
        reply += " {} became paralyzed!".format(opponent.name)

    return reply

def pound(self, opponent):
    damage, reply = self.standard_damage(self.level, 40, opponent)

    return reply

def karate_chop(self, opponent):
    damage, reply = self.high_crit_damage(self.level, 50, opponent)

    return reply

def double_slap(self, opponent):
    if (0.85 > random.random()):
        damage, reply = self.standard_damage(self.level, 15, opponent)

        num = random.random()

        if (0.125 > num):
            opponent.hitpoints -= damage * 4
            reply = "{} 5 hits! {}'s HP fell to {}!".format(self.critical_hit, opponent.name, str(opponent.hitpoints))

        elif (0.25 > num):
            opponent.hitpoints -= damage * 3
            reply = "{} 4 hits! {}'s HP fell to {}!".format(self.critical_hit, opponent.name, str(opponent.hitpoints))
        
        elif (0.625 > num):
            opponent.hitpoints -= damage * 2
            reply = "{} 3 hits! {}'s HP fell to {}!".format(self.critical_hit, opponent.name, str(opponent.hitpoints))
        else:
            opponent.hipoints -= damage
            reply = "{} 2 hits! {}'s HP fell to {}!".format(self.critical_hit, opponent.name, str(opponent.hitpoints))

    else:
        reply = "It missed! "

    return reply

move_methods = [
("bite", bite),
("bubble", bubble),
("leech life", leech_life),
("harden", harden),
("rock slide", rock_slide),
("agility", agility),
("dragon rage", dragon_rage),
("string shot", string_shot),
("seismic toss", seismic_toss),
("submission", submission),
("jump kick", jump_kick),
("horn drill", horn_drill),
("recover", recover),
("night shade", night_shade),
("poison sting", poison_sting),
("acid", acid),
("poison powder", poison_powder),
("toxic", toxic),
("smog", smog),
("sludge", sludge),
("poison gas", poison_gas),
("lick", lick),
("pound", pound),
("karate chop", karate_chop),
("double slap", double_slap)
]

