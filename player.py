from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, name):
        self.token = None
        self.opponent = None
        self.name = name
        super(Player, self).__init__()

    @abstractmethod
    def make_a_move(self):
        pass
