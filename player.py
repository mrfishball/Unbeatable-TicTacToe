from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, name):
        self.token = None
        self.name = name
        super(Player, self).__init__()

    def get_name(self):
        return self.name

    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token

    @abstractmethod
    def make_a_move(self):
        pass
