import time
import random

from . import items

class TrainerInput:
    def __init__(self, sender, message, hashmon_a, hashmon_b):
        if sender in (self.hashmon_a.trainer, self.hashmon_b.trainer):
            # Message format should be:
            # <hashmon_name>! use <move_name>!
        
            split_message = message.split('!')

            if len(split_message) > 1:
                self.hashmon_name = split_message[0]
                if self.hashmon_name == hashmon_a.name:
                    self.hashmon = hashmon_a
                elif self.hashmon_name == hashmon_b.name:
                    self.hashmon = hashmon_b

                self.action = split_message[1].strip().lower()

                if self.action in self.hashmon.moves:
                    pass
            
            self.trainer_name = sender

class HashmonBattle:
    def __init__(self, hashmon_a, hashmon_b):
        self.BATTLE_EXPIRY = 120
        self.hashmon_a = hashmon_a
        self.hashmon_b = hashmon_b
        self.battling = True
        self.battle_timer = time.time()
        self.previous_timer = time.time()
        self.a_action = None
        self.b_action = None
    
    def apply_one_move(self, hashmon, move, opponent):
        reply = ""

        # Normal status.
        if hashmon.status == "normal":
            reply += hashmon.move(opponent, move)
        
        # Poisoned status. Take 1/16 of max HP as damage after doing move.
        elif hashmon.status == "poisoned":
            reply += hashmon.move(opponent, move)
            
            hashmon.hitpoints -= int((hashmon.max_hitpoints / 16) + 1)
            reply += " {} is poisoned! HP fell to {}!".format(hashmon.name,
                                                        str(hashmon.hitpoints))

        elif hashmon.status == "paralyzed":
            if (0.25 > random.random()):
                reply += " {} is paralyzed!".format(hashmon.name)

            else:
                reply += hashmon.move(opponent, move)

        fainted = self.faint_check(opponent)
        
        if fainted:
            return reply + fainted

        fainted = self.faint_check(hashmon)

        if fainted:
            return reply + fainted

        return reply

    def faint_check(self, hashmon):
        # Check if hashmon fainted.
        if hashmon.hitpoints < 1: 
            self.battling = False
            return " " + hashmon.name + " fainted!"

        # This isn't necessary at all, but it explains to me what's up.
        else:
            return None

    def apply_moves(self, first_hashmon, first_move, second_hashmon, second_move):
        reply = ""

        reply += self.apply_one_move(first_hashmon, first_move, second_hashmon)

        if self.battling:
            reply += " " + self.apply_one_move(second_hashmon, second_move, first_hashmon)
        
        # Remember to clear the actions after doing all the moves.
        self.a_action = None
        self.b_action = None

        return reply
    
    def take_turn(self, sender, message):
        
        self.previous_timer = self.battle_timer
        self.battle_timer = time.time()
        
        if (time.time() - self.previous_timer) > self.BATTLE_EXPIRY:
            print("Battle draw.")
            self.battling = False

            return None

        if sender in (self.hashmon_a.trainer, self.hashmon_b.trainer):
            # Message format should be:
            # <hashmon_name>! use <move_name>!
            split_message = message.split('!')
            
            if len(split_message) > 1:
                name = split_message[0]
                action = split_message[1].strip()
                action = action.lower()
            
            else:
                return None

            if (sender == self.hashmon_a.trainer and
                    name == self.hashmon_a.name and
                    self.a_action is None):
                
                if "use " in action:
                    self.a_action = "".join(action.split("use ")).strip()
                
                else:
                    self.a_action = action

                print("Action is: " + self.a_action)

            elif (sender == self.hashmon_b.trainer and
                    name == self.hashmon_b.name and
                    self.b_action is None):
                
                if "use " in action:
                    self.b_action = "".join(action.split("use ")).strip()

                else:
                    self.b_action = action

        if self.a_action and self.b_action:
            # Determine which hashmon goes first.
            if self.hashmon_a.speed >= self.hashmon_b.speed:
                return self.apply_moves(self.hashmon_a, self.a_action, self.hashmon_b, self.b_action)
            else:
                return self.apply_moves(self.hashmon_b, self.b_action, self.hashmon_a, self.a_action)

        self.battle_timer = self.previous_timer
