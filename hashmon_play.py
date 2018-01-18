from hashmon import hashmon

if __name__ == '__main__':
    hashmond = hashmon.HashmonGame()
    hashmond.WILD_TIMER = 1
    while True:
        a = input()
        print(hashmond.update(a, 'playerone'))
