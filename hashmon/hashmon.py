import re
import time
import random

from . import hashmon_maker
from . import hashmon_battle
#from . import guardian
from . import hashmon_trainers

class HashmonGame:

    def __init__(self):
        self.chat_name = "hashmonhost"
        self.wild_name = "Charmander"

        self.state = 'idle'
        self.WILD_TIMER = 20
        self.start_timer = 0
        self.hashmon_a = None
        self.hashmon_b = None
        self.trainers = ''
        #self.load_trainers()
        self.battle = None

        self.trainers = hashmon_trainers.Trainers(4)

    """def save_trainers(self):
        ''' Save trainers to file. '''
        print('Saving trainers...')
        # Change this stuff to print(yadda_yadda, file=open())
        with open('trainers.txt', 'w', encoding='UTF-8') as f:
            for (trainer, items) in self.trainers.items():
                f.write(trainer + ';' + ';'.join(items) + '\n')

    def load_trainers(self):
        ''' Load trainers from file. '''
        print('Loading trainers...')
        # Change this stuff to print(yadda_yadda, file=open())
        with open('trainers.txt', 'r', encoding='utf8') as f:
            trainers = f.readlines()
        self.trainers = {}
        for line in trainers:
            line = line.rstrip()
            ar = line.split(';')
            self.trainers[ar[0]] = ar[1:]

    def add_item(self, trainer, item):
        ''' Add an item to a trainer's inventory. '''
        if trainer not in self.trainers:
            self.trainers[trainer] = []
        if item not in self.trainers:
            self.trainers[trainer].append(item)
        self.save_trainers()

    def remove_item(self, trainer, item):
        ''' Remove an item from a trainer's inventory. '''
        if trainer in self.trainers and item in self.trainers[trainer]:
            self.trainers[trainer].remove(item)
        self.save_trainers()"""

    def stats_string(self, the_hashmon):
        return "ATK: {} DEF: {} SPD: {} HP: {}".format(
                str(the_hashmon.attack), str(the_hashmon.defense),
                str(the_hashmon.speed), str(the_hashmon.hitpoints)
                )

        #return "ATK: " + str(the_hashmon.attack) + " DEF: " + str(the_hashmon.defense) + " SPD: " + str(the_hashmon.speed) + " HP: " + str(the_hashmon.hitpoints)
    def show_stats(self, message, sender):
        name = message

        the_hashmon = hashmon_maker.make_hashmon(sender, name)

        return name + "'s stats are | " + self.stats_string(the_hashmon)
    
    def _state_idle(self, message, sender):
        if re.search('^\S+! I choose (you|YOU)!$', message):
            self.state = 'starting'
            self.start_timer = time.time()
            name = message.split(' ')[0][:-1]
            self.hashmon_a = hashmon_maker.make_hashmon(sender, name)
            return "{} sent out {}! {}".format(
                    sender, name, self.stats_string(self.hashmon_a
                    )
            )

        else:
            return None

    def update(self, message, sender):
        if self.state == 'idle':
            return self._state_idle(message, sender)

            """if re.search('^\S+! I choose (you|YOU)!$', message):
                self.state = 'starting'
                self.start_timer = time.time()
                name = message.split(' ')[0][:-1]
                self.hashmon_a = hashmon_maker.make_hashmon(sender, name)
                #self.hashmon_a.trainer = sender
                return "{} sent out {}! {}".format(
                        sender, name, self.stats_string(self.hashmon_a
                        )
                                            )
                #return sender + ' sent out ' + name + '! ' + self.stats_string(self.hashmon_a)

            else:
                return None"""

        elif self.state == 'starting':
            sent_out = re.search('^\S*! I choose (you|YOU)!$', message)

            if (sender != self.hashmon_a.trainer and sent_out):
                name = message.split(' ')[0][:-1]
                self.hashmon_b = hashmon_maker.make_hashmon(sender, name)
                #self.hashmon_b.trainer = sender
                self.state = 'battling'
                self.battle = hashmon_battle.HashmonBattle(
                        self.hashmon_a, self.hashmon_b
                        )

                return "{} sent out {}! {} Battle start!".format(
                        sender, name, self.stats_string(self.hashmon_b)
                        )

                #return sender + ' sent out ' + name + "! " + self.stats_string(self.hashmon_b) + ' Battle start!'

            if time.time() - self.start_timer > self.WILD_TIMER:
                self.start_timer = 0

                # Check if trainer who sent out is eligible to battle a wild.
                eligible_to_play = self.trainers.can_play(self.hashmon_a.trainer)
                print(eligible_to_play)

                if eligible_to_play:
                    self.wild_name = random.choice(open("pokemon_names.txt", "r").readlines()).strip()
                    self.hashmon_b = hashmon_maker.make_hashmon(self.chat_name, self.wild_name)
                    self.state = 'battling'
                    self.battle = hashmon_battle.HashmonBattle(
                            self.hashmon_a, self.hashmon_b
                            )

                    return 'A wild ' + self.wild_name + ' appeared! What will ' + str(self.hashmon_a.name) + ' do? ' + self.stats_string(self.hashmon_b)
                else:
                    self.state = "idle"

        elif self.state == 'battling':
            if not self.battle.battling:
                self.battle = None
                self.state = 'idle'
                return self.update(message, sender)

            if self.hashmon_b.trainer == self.chat_name:
                #print(self.wild_name)
                self.battle.take_turn(self.chat_name, self.wild_name + '! FIGHT!')

            reply = self.battle.take_turn(sender, message)
            return reply


def main_loop():
    hashmon = HashmonGame()
    while True:
        a = input()
        print(hashmon.update(a, 'playerone'))
        b = input()
        print(hashmon.update(b, 'playertwo'))


if __name__ == "__main__":
    main_loop()
