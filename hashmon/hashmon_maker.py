from types import MethodType

from . import hasher
from . import hashmon_animal
from .hashmon_move_methods import move_methods

def make_hashmon(sender, name):
    hash_number = hasher.make_hash(name)
    hash_string = str(hash_number)

    hash_list = []
    # Up to digit 3 of hash. attack
    hash_list.append(sum([int(d) for d in list(hash_string[:3])]))
    # Up to digit 6 of hash. defense
    hash_list.append(sum([int(d) for d in list(hash_string[3:6])]))
    # Up to digit 9 of hash. hitpoints
    hash_list.append(sum([int(d) for d in list(hash_string[6:9])]))
    # Up to digit 12 of hash. special
    hash_list.append(sum([int(d) for d in list(hash_string[9:12])]))
    # Up to digit 15 of hash. speed
    hash_list.append(sum([int(d) for d in list(hash_string[12:15])]))

    # Up to digit 18 of hash. move
    moves_list = move_methods
    the_move = moves_list[sum([int(d) for d in list(hash_string[15:18])]) % len(moves_list) - 1 ]
    # Up to digit 21 of hash. move 2 
    the_move2 = moves_list[sum([int(d) for d in list(hash_string[18:21])]) % len(moves_list) - 1 ]

    #print(hash_list)
    # Arguments are:
    # trainer, name='', attack=0, defense=0, hitpoints=0, special=0,
    # speed=0
    hashmon = hashmon_animal.Hashmon(sender, name, *hash_list)

    # This is probably really bad practice.
    hashmon.moves[the_move[0]] = MethodType(the_move[1], hashmon)
    hashmon.moves[the_move2[0]] = MethodType(the_move2[1], hashmon)

    print(hashmon.name)
    print(the_move[0], the_move2[0])

    return hashmon

if __name__ == '__main__':
    while True:
        a = input()
        make_hashmon('playerone', a)

