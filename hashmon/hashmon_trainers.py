from time import time


class Trainer:
    def __init__(self, name, timer, items):
        self.name = name
        self.timer = timer
        self.items = items
    def add_item(self, item):
        """Add an item to a trainer's inventory."""
        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item):
        """Remove an item from a trainer's inventory."""
        if item in self.items:
            self.items.remove(item)


class Trainers:
    """Manage trainer inventories and replay timers."""
    def __init__(self, replay_time):
        self.replay_time = replay_time
        self.load_trainers()

    def save_trainers(self):
        """Save trainers to file."""
        print('Saving trainers...')
        
        with open('trainers.txt', 'w', encoding='UTF-8') as f:
            for name, trainer in self.trainers.items():
                f.write("{};{};{}\n".format(
                        trainer.name,
                        trainer.timer,
                        ";".join(trainer.items)
                    )
                )

    def load_trainers(self):
        """Load trainers from file."""
        print('Loading trainers...')

        with open('trainers.txt', 'r', encoding='utf8') as f:
            trainers = f.readlines()

        self.trainers = {}
        for line in trainers:
            line = line.rstrip()
            split_line = line.split(';')
            name = split_line[0]
            timer = split_line[1]
            items = split_line[2:]
            self.trainers[name] = Trainer(name, timer, items)

    def add_item(self, trainer, item):
        if trainer in self.trainers:
            self.trainers[trainer].add_item(item)
            self.save_trainers()
            print("Added {} to {}'s inventory.".format(item, trainer))

    def remove_item(self, trainer, item):
        if trainer in self.trainers:
            self.trainers[trainer].remove_item(item)
            self.save_trainers()
            print("Removed {} from {}'s inventory.".format(item, trainer))

    def _set_timer(self, trainer, timer):
        if trainer in self.trainers:
            self.trainers[trainer].timer = str(timer)
            self.save_trainers()
        else:
            self.trainers[trainer] = Trainer(trainer, str(timer), [])
            self.save_trainers()

    def _get_timer(self, trainer):
        if trainer in self.trainers:
            print(self.trainers[trainer].name)
            print(self.trainers[trainer].timer)
            return int(self.trainers[trainer].timer)
        else:
            self.trainers[trainer] = Trainer(trainer, "0", [])
            return 0

    def can_play(self, trainer):
        timer = self._get_timer(trainer)

        if (time() - timer) > self.replay_time:
            self._set_timer(trainer, int(time()))
            return True

        else:
            return False
