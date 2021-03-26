class GotCharacter:
    """This is the representation of the GotCharacter class"""

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """prints to screen the House words"""

        print(self.house_words)

    def die(self):
        """changes the value of is_alive to False"""

        self.is_alive = False


class Lannister(GotCharacter):
    """A class representing the Lannister family. House Lannister of Casterly Rock."""

    def __init__(self, first_name=None, is_alive=True):
        super(Lannister, self).__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar!"
